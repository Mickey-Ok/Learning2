
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate,login, logout 
from django.contrib.auth.models import User,auth
from django.contrib import messages 
# from django.contrib.auth.decorators import login_required

# Create your views here.
def homeview (request):
    return render (request,'view.html',{}) 

def logoutview(request):
    logout(request)
    return render(request,'view.html',{})  

# @login_required
def loginview(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(request,email=email, password=password) 

        if user is not None:
            login(request,user)
            return redirect('accounts')
        else:
            messages.error(request, 'Email Or Password is INCORRECT') 
            return redirect('login')
      
    # context={}
    else:
     return render (request,'registration/login.html', {})



def registerview(request):
    if request.method == 'POST':
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password1']
        password2=request.POST['password2']
      
        if password==password2:
         if  User.objects.filter(email=email).exists():
             messages.info(request, 'Email is Taken Already!!')
             return redirect ('register')
         elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username is Taken Already!!') 
                return redirect ('register')
         else:
                user=User.objects.create_user(username=username, email=email, password=password)
                user.save() 
                return redirect('accounts')
        else:
            messages.info(request,'Passwords are NOT MATCHING!!')
            return redirect ('register')
    else:
      return render(request, 'registration/register.html',{}) 
    
# def accountview(request): 
#     return render(request,'accounts.html',{})

def contentview (request):
    return render (request,'contents.html',{}) 
