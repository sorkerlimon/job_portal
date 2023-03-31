from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required,user_passes_test
from users.decorators import *

# Create your views here.



@login_required(login_url='register')
@allowed_users(allowed_roles=['employee'])
def job_board(request):
    employee_profile = request.user.employee_profile

    
    return render(request, 'job/joblist.html', {'employee_profile': employee_profile})