import logging
from sbte.models import User
from django.shortcuts import render, redirect
from sbte.forms import UserRegisterationForm, UserLoginForm
from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout, authenticate, login
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash
from sbte.forms import UserPasswordChangeForm
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from utils.helpers import send_forget_password_email


db_logger = logging.getLogger('db')

def HomeView(request):
    return render(request, 'home.html')


"""User SignUp View"""
def UserSignUpView(request):
    form  = UserRegisterationForm()
    if request.method == "POST":
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            print('1')
            user = form.save()
            print(user)
            login(request, user)
            if user.user_type == 'A':
                return redirect('admindashboard-view')
            elif user.user_type == 'IS':
                return redirect('institutedashboard-view')
            else:
                return redirect('studentdashboard-view')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = UserRegisterationForm()
    return render (request=request, template_name="basic/registration.html", context={"form":form})



"""User Login View"""
def UserLoginView(request) : 
    form  = UserLoginForm()
    if request.method == 'POST': 
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = authenticate(email = email,password=password)
            id=User.objects.get(email=email).pk
            if user is not None :
                try:
                    login(request, user)
                    db_logger.info(f'Login,User Type-{user.user_type}')    
                    if user.is_passupdated == 1:
                        if user.user_type == 'A':
                            return redirect('admindashboard-view')
                        elif user.user_type == 'IS':
                            return redirect('institutedashboard-view')
                        else:
                            return redirect('studentdashboard-view')
                    else:
                        return redirect('changepassword-view',id)    
                except Exception as e:
                    db_logger.exception(e)    
            else:
                return HttpResponse("Invalid Credential for Login !!")
        messages.error(request,"Please Correct Below Errors")
    form = UserLoginForm()
    return render(request, "basic/login.html",{"form":form})


"""Change password View"""
@login_required
def UserChangePasswordView(request,id):
    obj =User.objects.filter(id=id)
    if request.method == 'POST':
        form = UserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            try:
                user = form.save()
                update_session_auth_hash(request, user)
                messages.success(request,'Your password was successfully updated!')
                obj.update(is_passupdated=True)
                db_logger.info(f'password changed,User Type-{user.user_type}')  
                return redirect('logout-view') 
            except Exception as e:
                db_logger.exception(e)  
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserPasswordChangeForm(request.user)
    return render(request, 'basic/changepassword.html', {'form': form})


"""User Logout View"""
def UserLogoutView(request):
    logout(request)
    return redirect('home-view')





