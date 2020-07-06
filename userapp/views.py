from django.shortcuts import render

# Create your views here.
# from rest_framework import request
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt import settings
#查看各个token类的入口
from rest_framework_jwt.views import JSONWebTokenAPIView

from utils.response import APIResponse
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
    def post(self,request,*args,**kwargs):
        user_ser = UserModelSerializer(data=request.data)
        user_ser.is_valid(raise_exception=True)
        return APIResponse(data_message="success",token=user_ser.token, results=UserModelSerializer(user_ser.obj).data)



