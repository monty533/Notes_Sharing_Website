from django.contrib import admin
from django.urls import path , include
from gym import views

urlpatterns = [
    path('', views.index_view, name='home'),
    path('about/', views.about_view, name='About'),
    path('contact/', views.contact_view, name='Contact'),
    path('adminlogin/', views.adminlogin_view, name='Adminlogin'),
    path('logout/', views.logout_view, name='Logout'),
    
    path('addenquiry/', views.addenquiry_view, name='Addenquiry'),
    path('viewenquiry/', views.viewenquiry_view, name='Viewenquiry'),
    path('delete_enquiry(?p<int:pid>)/', views.Delete_Enquiry_view, name='Delete_enquiry'),

    path('addequipment/', views.addequipment_view, name='Addequipment'),
    path('viewequipment/', views.viewequipment_view, name='Viewequipment'),
    path('delete_equipment(?p<int:pid>)/', views.delete_equipment_view, name='Delete_equipment'),

    path('add_plan/', views.add_plan_view, name='Add_plan'),
    path('view_plan/', views.view_plan_view, name='View_plan'),
    path('delete_plan/<int:pid>/', views.delete_plan_view, name='Delete_plan'),

    path('add_member/', views.add_member_view, name='Add_member'),
    path('view_member/', views.view_member_view, name='View_member'),
    path('delete_member/<int:pid>/', views.delete_member_view, name='Delete_member'),

]