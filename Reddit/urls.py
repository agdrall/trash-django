"""Reddit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home_redirect, name = 'home_redirect'), # when you go to empty url, it will redirect to home 

    url(r'^admin/', admin.site.urls),
    url(r'^user_accounts/', include('user_accounts.urls', namespace = 'user_accounts')), #this url sets up all the urls in the user_accounts app. 
    url(r'^home/', include('home.urls', namespace = 'home')),
]

