import os.path

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import permissions, mixins

from TestPlatformApi import settings
from TestProject.models import TestProject, TestEnv, TestFile
from .serializer import TestProjectSerializer, TestEnvSerializer, TestFileSerializer


# Create your views here.
# 测试项目管理  增删查改接口的实现
class TestProjectView(ModelViewSet):
    """测试项目视图集"""
    queryset = TestProject.objects.all()
    serializer_class = TestProjectSerializer
    # 添加视图的权限校验（需要登录才能访问，访问的时候需要在请求头中添加token）
    permission_classes = [permissions.IsAuthenticated]


# 测试环境管理的接口开发(增删改查)
class TestEnvView(ModelViewSet):
    queryset = TestEnv.objects.all()
    serializer_class = TestEnvSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['project', ]


# 测试文件管理的接口开发（上传、删除、获取文件列表）
class TestFileView(mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    """测试文件管理"""
    queryset = TestFile.objects.all()
    serializer_class = TestFileSerializer

    def create(self, request, *args, **kwargs):
        """文件上传的方法"""
        # 文件大小不能超过300kb
        # 获取上传文件的大小
        size = request.data['file'].size
        name = request.data['file'].name
        if size > 1024 * 300:
            return Response({'error': '文件大小不能超过300KB！'}, status=400)
        if os.path.isfile(settings.MEDIA_ROOT / name):
            return Response({'error': '文件已存在，不能重复上传！'}, status=400)
        # 文件不能重复上传
        return super().create(request, *args, **kwargs)
