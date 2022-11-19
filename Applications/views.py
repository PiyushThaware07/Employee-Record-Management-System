from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request, 'apps/index.html')

def emp_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            error = "no"
        else:
            error = "yes"    

    return render(request, 'apps/emp_login.html',locals())

def emp_signup(request):
    if request.method == "POST":
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password1']

        error = ""
        try:
            new_user = User.objects.create_user(first_name=fname,last_name=lname,username=email,password=password)   
            error = 'no'
        except:
            error = 'yes'    
    return render(request, 'apps/emp_signup.html',locals())