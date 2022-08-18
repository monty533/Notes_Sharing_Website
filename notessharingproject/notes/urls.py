from django.contrib import admin
from django.urls import path , include
from notes import views
from notes.models import *

urlpatterns = [
    path('',views.index_view,name='Home'),
    path('about/',views.about_view,name='about'),
    path('contact/',views.contact_view,name='contact'),
    path('login/',views.userlogin_view,name='userlogin'),
    path('adminlogin/',views.adminlogin_view,name='adminlogin'),
    path('signup/',views.signup_view,name='signup'),
    path('adminhome/',views.adminhome_view,name='adminhome'),
    path('profile/',views.profile_view,name='profile'),

]
