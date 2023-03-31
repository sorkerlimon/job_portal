from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required,user_passes_test
from users.models import *
from .forms import *
from users.forms import *
from django.utils import timezone
from .agreement import *
from users.decorators import *
from django.core.files.base import ContentFile
import cv2
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseBadRequest


# Create your views here.

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

@login_required(login_url='register')
@allowed_users(allowed_roles=['employee'])
def privacy_polic(request):
    employee_profile = request.user.employee_profile

    
    return render(request, 'employee/poli_priva.html', {'employee_profile': employee_profile})



@login_required(login_url='register')
@allowed_users(allowed_roles=['employee'])
def dashboard(request):
    employee_profile = request.user.employee_profile
    show_secret_key_div = not employee_profile.has_used_secret_key

    if request.method == 'POST':
        name = request.POST['secretkey']
        if name == 'limon@123':
            employee_profile.has_used_secret_key = True
            employee_profile.save()
            show_secret_key_div = False
        else:
            return HttpResponse("Incorrect Code")
    
    return render(request, 'employee/emp_dashboard.html', {'show_secret_key_div': show_secret_key_div,'employee_profile': employee_profile})



@login_required(login_url='register')
@allowed_users(allowed_roles=['employee'])
def upload(request):
    current_user = request.user.employee_profile
    employee_profile = request.user.employee_profile
    
    form = Employee_CVForm()
    
    if request.method == 'POST':
        form = Employee_CVForm(request.POST, request.FILES)
        if form.is_valid():

            country = form.cleaned_data['country']
            fullname = form.cleaned_data['fullname']
            phonenumber = form.cleaned_data['phonenumber']
            dateofbirth = form.cleaned_data['dateofbirth']
            education = form.cleaned_data['education']
            nationalid = form.cleaned_data['nationalid']


            instance = form.save(commit=False)
            instance.p_user = current_user
            instance.save()

            # Create or update Employee_profile model
            employee_profile.name = fullname
            employee_profile.phone = phonenumber
            employee_profile.nid = nationalid
            employee_profile.dob = dateofbirth
            employee_profile.country = country
            employee_profile.education_degree = education
            employee_profile.save()
            
            # return redirect('profile')
            return HttpResponse('your document upload is complete')
        else:
            print(form.errors)
            error_message = "Form submission failed: please check the form fields and try again."
            return HttpResponse(error_message)

    context = {
        'form': form,
        'employee_profile':employee_profile,
     
    }
    return render(request, 'employee/upload.html', context)

@login_required(login_url='register')
@allowed_users(allowed_roles=['employee'])
def documents_upload(request):
    current_user = request.user.employee_profile
    employee_profile = request.user.employee_profile
    
    form = Documents_upload_form()
    
    if request.method == 'POST':
        form = Documents_upload_form(request.POST, request.FILES)
        if form.is_valid():
            
            instance = form.save(commit=False)
            instance.p_user = current_user
            instance.save()
            return redirect('profile')
        else:
            print(form.errors)
            error_message = "Form submission failed: please check the form fields and try again."
            return HttpResponse(error_message)

    context = {
        'form': form,
        'employee_profile':employee_profile,
     
    }
    return render(request, 'employee/documnetsupload.html', context)




# Profile Complete code started here #

@login_required(login_url='register')
@allowed_users(allowed_roles=['employee'])
def profile(request):
    profile = request.user
    employee_profile = request.user.employee_profile

    info = dict()
    

    if request.method == 'POST':
        form = ProfleForm(request.POST,  request.FILES,instance=employee_profile)
        if form.is_valid():
            info['uname'] = form.cleaned_data['name']
            info['nid'] = form.cleaned_data['nid']
            info['present_address'] = form.cleaned_data['present_address']
            info['phone'] = form.cleaned_data['phone']
            info['email'] = form.cleaned_data['email']
            info['dob'] = form.cleaned_data['dob']
            info['education_degree'] = form.cleaned_data['education_degree']
           
            agreement = agreement_generator(info)

            ret, buf = cv2.imencode('.jpg', agreement[0]) 
            content = ContentFile(buf.tobytes())     

            ret2, buf2 = cv2.imencode('.jpg', agreement[1]) 
            content2 = ContentFile(buf2.tobytes())

            employee_profile.agreement_1.save(f"{info['nid']}_page_1.jpg", content)
            employee_profile.agreement_2.save(f"{info['nid']}_page_2.jpg", content2)

            form.save()

            return redirect('profile')
    else:
        form = ProfleForm(instance=employee_profile)

    context = {'form':form,'profile':profile,'employee_profile':employee_profile}
    return render(request,'employee/profile.html', context)






@login_required(login_url='register')
@allowed_users(allowed_roles=['employee'])
def agrement(request,pk):
    profile = request.user
    employee_profile = request.user.employee_profile

    agrements_paper = Employee_profile.objects.get(id=pk)
    



    context = {'profile':profile,'employee_profile':employee_profile,'agrements_paper':agrements_paper}
    return render(request,'employee/agreement.html', context)

                                                        # HR Management Complete code started here #


# HR Dashboard Complete code started here #

@login_required(login_url='register')
@allowed_users(allowed_roles=['hr'])
def hrdashboard(request):
    employee_profile = request.user.employee_profile
    context = {'employee_profile': employee_profile}
    return render(request, 'hr_templates/hr_dashboard.html',context)


# HR UserManagement Complete code started here #
@login_required(login_url='register')
@allowed_users(allowed_roles=['hr'])
def user_management(request):
    employee_profile = request.user.employee_profile

    all_user = Employee_CV.objects.filter(meet_link_sent=False).select_related('p_user')
    all_user_complete = Employee_CV.objects.filter(meet_link_sent=True).select_related('p_user')
    # dashboard_complete = Employee_CV.objects.filter(meet_link_sent=True, p_user__license=True).select_related('p_user')
    
    context = {'all_user': all_user,'all_user_complete': all_user_complete,'employee_profile':employee_profile,}
    return render(request,'hr_templates/user_management.html',context)

# HR Send Meet link  Complete code started here #
def send_meet_link(request):
    if request.method == 'POST':
        selected_users = request.POST.getlist('tag')
        for user_id in selected_users:
            employee_cv = Employee_CV.objects.get(p_user_id=user_id)
            meet_link = 'https://meet.google.com/qje-zrpa-nem'
            send_mail(
                'Your meet link',
                f'Here is your meet link: {meet_link}',
                'nawrafilim2023@gmail.com',
                [employee_cv.p_user.user.email],
                fail_silently=False,
            )
            employee_cv.meet_link_sent = True
            employee_cv.save()
        messages.success(request, 'Meet links sent successfully')
        return redirect('user_management')
    else:
        return HttpResponseBadRequest('Invalid request method')





# HR Management Complete code End here #





def user_list(request):
    now = timezone.now()
    active_users = User.objects.filter(last_login__gte=now - timezone.timedelta(hours=24))
    inactive_users = User.objects.exclude(last_login__gte=now - timezone.timedelta(hours=24))
    employee_profiles = Employee_profile.objects.filter(user__in=active_users | inactive_users)
    context = {'active_users': active_users, 'inactive_users': inactive_users, 'employee_profiles': employee_profiles}
    return render(request, 'hr_templates/active_deactive_user.html', context)





