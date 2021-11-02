"""CS_303 URL Configuration

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
from django.urls import path, include
from slot_details import views as slot_view
from stats import views as stat
from notifications import views as subscribe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', stat.statewise, name='stats'),
    path('slots/', slot_view.state_list, name='dist_details'),
    path('subscribe/', subscribe.user_subscription, name='subscription')
]
