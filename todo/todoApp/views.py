from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate,login as auth_login


def login(request):
    if request.method=='POST':
        username=request.POST['email']
        password=request.POST['password']
        
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('base')
        else:
            messages.info(request,'invalid credentials')
            return redirect('/')        
    else:
        return render(request,'login.html')


def signup(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        
        if pass1==pass2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already registered')
                return redirect('signup')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=email, email=email,password=pass1)
                user.save()
                return redirect('success')
                
        else:
            messages.info(request,'Password not matching')
            return redirect('signup')
        
    else:
        return render(request,'signup.html')

def base(request):
    return render(request,'base.html')

def success(request):
    return render(request,'success.html')

def logout(request):
    auth.logout(request)
    return redirect('/')