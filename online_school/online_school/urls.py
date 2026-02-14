"""online_school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

import entry.views
import user_profile.views
import user_chats.views
import user_schedule.views

urlpatterns = [
    path('', entry.views.main_page),
    path('/', entry.views.main_page),
    path('admin/', admin.site.urls),
    path('entry/', entry.views.main_page),
    path('user_profile/', user_profile.views.main_page),
    path('user_chats/', user_chats.views.main_page),
    path('user_schedule/', user_schedule.views.main_page),
]
