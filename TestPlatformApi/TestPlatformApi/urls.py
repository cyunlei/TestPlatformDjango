"""TestPlatformApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Users.views import LoginView, LoginTokenRefreshView, LoginTokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    # 登录接口的访问路径
    path('api/users/login/', LoginView.as_view(), name='login'),
    # 刷新token
    path('api/users/token/refresh/', LoginTokenRefreshView.as_view(), name='token_refresh'),
    # 校验token有效
    path('api/users/token/verify/', LoginTokenVerifyView.as_view(), name='token_verify'),
]
# 导入def的路由和自定义的视图集
from rest_framework import routers
from TestProject.views import TestProjectView, TestEnvView, TestFileView

# # 创建一个对应对象
# router = routers.SimpleRouter()
# # 注册项目管理的路由
# router.register('api/testPro/projects/', TestProjectView)
# # 注册测试环境管理的路由
# router.register('api/testPro/envs/', TestEnvView)
# #
# router.register('api/testPro/files', TestFileView)
#
# urlpatterns += router.urls
