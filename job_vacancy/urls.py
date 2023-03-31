
from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path('upload/', upload,name='upload'),
    path('privacy_polic/', privacy_polic,name='privacy_polic'),
    path('sucessfully/', sucessfulmessage,name='sucessfulmessage'),


    path('documentsupload/', documents_upload,name='documentsupload'),
    # path('currentjoboffer/', currentjob,name='currentjoboffer'),


    path('hrdashboard/', hrdashboard,name='hrdashboard'),
    # path('upload/', upload,name='upload'),
    path('dashboard/', dashboard,name='dashboard'),
    path('agrement/<str:pk>/', agrement,name='agrement'),



    path('user_management/', user_management,name='user_management'),
    path('', profile, name='profile'),
    path('user-list/', user_list, name='user_list'),
    path('send-meet-link/', send_meet_link, name='send_meet_link'),

    path('404/', page_not_found_view, name='404'),
   
    

]

handler404 = 'job_vacancy.views.page_not_found_view'