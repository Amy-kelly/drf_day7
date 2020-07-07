from django.conf.urls import url
from django.urls import path
from rest_framework_jwt.views import ObtainJSONWebToken, obtain_jwt_token,VerifyJSONWebToken

from userapp import views

urlpatterns = [
    url(r"test/",ObtainJSONWebToken.as_view()),
    # url(r"test1/",VerifyJSONWebToken.as_view()),
    url(r"test2/",obtain_jwt_token),
    path("name/",views.UserAPIView.as_view()),
    path("login/",views.ManyLoginAPIView.as_view()),
    path("coffees/",views.CoffeeQueryAPIView.as_view())

]