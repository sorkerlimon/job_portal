from django.shortcuts import render,HttpResponse,redirect

from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .decorators import *
from django.core.mail import send_mail
import random

from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_str
from django.core.mail import EmailMessage
from .tokens import account_activation_token

from django.contrib.auth.tokens import default_token_generator
import secrets
import random
import string
import time
import smtplib
import pyotp
from email.mime.text import MIMEText

@unauthenticated_user
def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            
            # Check if an Employee_profile object with the given email already exists
            email = form.cleaned_data.get('email')
            employee_profile = Employee_profile.objects.filter(email=email).first()
            if not employee_profile:
                employee_profile = Employee_profile.objects.create(
                    user=user,
                    name=user.username,
                    phone=form.cleaned_data.get('phone'),
                    email=email,
                )

            current_site = get_current_site(request)
            mail_subject = 'An account has been'
            message = render_to_string('template_activate_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            send_mail = email
            print(send_mail)
            email = EmailMessage(mail_subject, message, to=[send_mail])
            email.send()
            messages.success(request, 'Check your email for Active acount')
            return redirect('loginpage')
        else:
            messages.error(request, 'Email or phone already exists.')
    else:
        form = CreateUserForm()

    return render(
        request=request,
        template_name="register.html",
        context={"form": form}
    )


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user=User._default_manager.get(pk=uid)
    except(TypeError,ValueError,User.DoesNotExist):
        user=None
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        messages.info(request, 'Your Account is activated now')
        return redirect('loginpage')
    

# Login Process Started Here
@unauthenticated_user
def loginpage(request):

    try:
        if request.method == 'POST':
            email = request.POST.get('username')
            password = request.POST.get('password')

            user = User.objects.get(email=email)
            

            if not user.is_active:
                messages.info(request, 'Your account is not activated check your Mail')
                return redirect('loginpage')
            
            user = authenticate(request, username=User.objects.get(email=email).username, password=password)
            if user is not None:
                messages.success(request,'Successfully Logged In')
                login(request,user)
                # return redirect('upload')
            for g in request.user.groups.all():
                if g.name == 'employee':
                    return redirect('upload')
                elif g.name == 'hr':
                    return redirect('hrdashboard')
            else:
                # print('Username or password not found')
                messages.error(request,'User name or password not found')

    except:
        return redirect('loginpage')
    context = {}
    return render(request, 'login.html',context)



# Login Process End Here

# Verify code with OTP Stated
 
# @unauthenticated_user
# def loginpage(request):

#     try:
#         if request.method == 'POST':
#             email = request.POST.get('username')
#             password = request.POST.get('password')

#             user = User.objects.get(email=email)
            
#             print("User .............",user)

#             if not user.is_active:
#                 messages.info(request, 'Your account is not activated check your Mail')
#                 return redirect('loginpage')
            
#             user = authenticate(request, username=User.objects.get(email=email).username, password=password)


#             if user is not None:
#                 otp = random.randint(1000, 9999) # Generate a 4-digit OTP
#                 subject = 'Login OTP'
#                 message = f'Your OTP for logging in is {otp}'
#                 from_email = 'nawrafilim2023@gmail.com'
#                 recipient_list = [email]
#                 send_mail(subject, message, from_email, recipient_list)

#                 # Store the OTP in the session so that it can be used later to verify
#                 request.session['otp'] = str(otp)
#                 request.session['email'] = email
#                 return redirect('verify_otp')
                
#             else:
#                 messages.info(request, 'Email or Password is incorrect')
#     except:
#         return redirect('loginpage')
#     context = {}
#     return render(request, 'login.html',context)



# def verify_otp(request):
#     if request.method == 'POST':
#         entered_otp = request.POST.get('otp')
#         if entered_otp == request.session.get('otp'):
#             # OTP verified, log the user in
#             user = User.objects.get(email=request.session.get('email'))
#             print(user)
#             login(request, user)
#             for g in request.user.groups.all():
#                 if g.name == 'employee':
#                     return redirect('upload')
#                 elif g.name == 'hr':
#                     return redirect('hrdashboard')
#         else:
#             messages.info(request, 'Incorrect OTP')

#     context = {}
#     return render(request, 'verify_otp.html', context)

# verify code ended 

def logoutuser(request):
    logout(request)
    return redirect('loginpage')




































# @unauthenticated_user
# def register(request):
    
#     form = CreateUserForm()

#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             username = form.cleaned_data.get('username')
            
#             messages.success(request,'Account created successfully ' + username)
#         return redirect('loginpage')

#     context = {'form': form}
#     return render(request, 'register.html',context)
# @unauthenticated_user
# def loginpage(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request,username=username,password=password)

#         if user is not None:
#             login(request,user)
#             return redirect('dashboard')
#         else:
#             messages.info('User Name or Password is incorrect')

#     context = {}
#     return render(request, 'login.html',context)

# @unauthenticated_user
# def loginpage(request):
#     if request.method == 'POST':
#         email = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=User.objects.get(email=email).username, password=password)

#         if user is not None:
#             login(request,user)
#             return redirect('dashboard')
#         else:
#             messages.info(request, 'Email or Password is incorrect')

#     context = {}
#     return render(request, 'login.html',context)
