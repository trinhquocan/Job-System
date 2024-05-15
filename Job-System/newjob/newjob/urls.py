"""
URL configuration for newjob project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.db import router
from django.urls import path, re_path, include
from anewjob.admin import admin_site
from rest_framework import routers
from anewjob import views

# router = routers.DefaultRouter()
# router.register('categories', views.CategoryViewSet, basename='categories')


urlpatterns = [
    path('', include('anewjob.urls')),
    # path('', include(router.urls)),
    path('admin/', admin_site.urls),
    re_path(r'^ckeditor/',include('ckeditor_uploader.urls'))
]
