"""
URL configuration for mysite2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from app1.views import index, function,API,community,about, admin

urlpatterns = [
    # path("admin/", admin.site.urls),

    # 管理员登录
    path("admin/register", admin.admin_register),
    # 管理员主页
    path("admin/index", admin.admin_index),
    # 前台流量
    path("admin/indexfront", admin.admin_indexfront),

    # 主页
    path("index/", index.index),

    # 功能
    path("function/", function.index),
    # 图片风格转换功能
    path("function/funTranPic/", function.funTranPic),

    # API
    path("API/", API.index),

    # 社区
    path("community/", community.index),

    # 关于
    path("about/", about.index),

]
