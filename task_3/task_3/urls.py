"""task_3 URL Configuration

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
from django.urls import path,include
from users_app import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # when you are at the main app please redirect to doubt_app.urls
    # It first look in the main project.urls file for the address
    # and then if it matches something, it send the remaining url to the app.urls for further relocating to the address
    path('doubt-app',include('doubt_app.urls')),
    path('register/',user_views.register, name = 'register'),
    path('accounts/', include('allauth.urls')),
]
