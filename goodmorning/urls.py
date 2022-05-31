"""goodmorning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from blog import views
# <> 안에 있는 건 int형, str형으로 받아서 넘길 것을 명시한 것
# detail_view 라는 함수가 PK라는 변수를 받아서 실행 / article_view라는 함수가 NAME이라는 변수를 받아서 실행
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.category_view, name='category'),
    path('new', views.new_view, name='new'),
    path('detail/<int:pk>', views.detail_view, name='detail'),
    path('<str:name>', views.article_view, name='article'),
]
