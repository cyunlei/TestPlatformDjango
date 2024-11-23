from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView,TokenVerifyView
import json


# Create your views here.
class LoginView(TokenObtainPairView):
    """自定义登录返回的字段数据"""

    # 登录
    # 重写父类方法
    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        # 自定义登录返回的字段
        result = serializer.validated_data
        result_data = {}
        result_data['token'] = result['access']
        result_data['refresh'] = result['refresh']

        return Response(result_data, status=status.HTTP_200_OK)


class LoginTokenRefreshView(TokenRefreshView):
    """自定义刷新登录token"""

    # 刷新token
    # 重写父类方法
    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        # 自定义登录返回的字段
        result = serializer.validated_data
        result_data = {}
        result_data['token'] = result['access']

        return Response(result_data, status=status.HTTP_200_OK)


class LoginTokenVerifyView(TokenVerifyView):
    """自定义验证登录token是否过期"""

    # 刷新token
    # 重写父类方法
    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        # 自定义登录返回的字段
        result = serializer.validated_data
        result_data = {}
        result_data['code'] = 200
        result_data['message'] = '验证成功！'

        return Response(result_data, status=status.HTTP_200_OK)
