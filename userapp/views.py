import re

from django.shortcuts import render

# Create your views here.
# from rest_framework import request
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt import settings
#查看各个token类的入口
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from rest_framework_jwt.views import JSONWebTokenAPIView

from utils.response import APIResponse
from .models import User
from .serializers import UserModelSerializer

class UserAPIView(APIView):
    #权限类  只允许认证通过的用户访问   游客无权访问
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]
    def get(self,request,*args,**kwargs):
        return APIResponse(results={"username":request.user.username})

class ManyLoginAPIView(APIView):
    authentication_classes = []
    permission_classes = []
    #面向对象
    def post(self,request,*args,**kwargs):
        user_ser = UserModelSerializer(data=request.data)
        user_ser.is_valid(raise_exception=True)
        return APIResponse(data_message="success",token=user_ser.token, results=UserModelSerializer(user_ser.obj).data)
    #面向过程
    def demo_post(self, request, *args, **kwargs):
        account = request.data.get("account")
        pwd = request.data.get("pwd")
        if re.match(r'.+@.+', account):
            user_obj = User.objects.filter(email=account).first()
        elif re.match(r'1[3-9][0-9]{9}', account):
            user_obj = User.objects.filter(phone=account).first()
        else:
            user_obj = User.objects.filter(username=account).first()

        # 判断用户是否存在 且用户密码是否正确
        if user_obj and user_obj.check_password(pwd):
            # 签发token
            payload = jwt_payload_handler(user_obj)  # 生成载荷信息
            token = jwt_encode_handler(payload)  # 生成token
            return APIResponse(results={"username": user_obj.username}, token=token)

        return APIResponse(data_message="error")

