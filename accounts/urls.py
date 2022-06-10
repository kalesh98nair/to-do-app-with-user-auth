from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('' , index , name="home"),
    path('login/' , Login , name="login"),
    path('register/' , Register , name="register"),
    path('forget-password/' , ForgetPassword , name="forget_password"),
    path('change-password/<token>/' , ChangePassword , name="change_password"),
    path('logout/' , Logout , name="logout"),
    path('index/', index, name="index"),
	path('update_task/<str:pk>/', updateTask, name="update_task"),
	path('delete/<str:pk>/', deleteTask, name="delete"),
]
