from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from core.models import *

# Create your views here.

def user_login(request):
      if request.method == "POST":
        pass
      username = request.POST.get('username')
      password= request.POST.get('password')
      print(username,password)
      return render(request,'accounts/login.html')

def user_register(request):
  if request.method == "POST":
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')
    phone= request.POST.get('phone_field')
    print(username,email,password,confirm_password,phone)
  
  return render(request,'accounts/register.html')

def user_logout(request):
   pass