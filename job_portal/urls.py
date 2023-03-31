
from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path('job_list/', job_board,name='job_portal'),


]

