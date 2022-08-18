from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('login',views.loginu, name='login'),
    path('logout',views.logoutu, name='logout'),
    
]
