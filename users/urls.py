
from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path('register/', register,name='register'),
    path('loginpage/', loginpage ,name='loginpage'),
    path('logout/', logoutuser ,name='logout'),
    # path('verify_otp/', verify_otp, name='verify_otp'),
    

    path('activate/<uidb64>/<token>',activate, name='activate'),
   
]
