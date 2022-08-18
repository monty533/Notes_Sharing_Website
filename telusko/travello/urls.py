from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='Index'),
    path('register/', views.register_view, name='Register'),
    path('about/', views.about_view, name='About'),
    path('login/', views.login_view, name='Login'),
    path('logout/', views.logout_view, name='Logout'),
    path('cities/', views.cities_view, name='Cities'),
    
    
]
