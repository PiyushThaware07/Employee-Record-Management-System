from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth import authenticate,login,logout
import random

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

def emp_logout(request):
    logout(request)
    return redirect('index')

def emp_signup(request):
    if request.method == "POST":
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password1']

        # Generate Emp_id
        max_length = 6
        digits = ['0','1','2','3','4','5','6','7','8','9']
        character = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','w','x','y','z']
        combine_list = digits + character
        temp = [random.choice(combine_list) for item in range(max_length)]
        emp_code = ""
        for element in temp:
            emp_code+=element
        emp_id = emp_code

        error = ""
        try:
            new_user = User.objects.create_user(first_name=fname,last_name=lname,username=email,password=password)   
            employee = EmployeeDetail.objects.create(user=new_user,empcode=emp_id)
            error = 'no'
        except:
            error = 'yes'    
    return render(request, 'apps/emp_signup.html',locals())

def emp_Interface(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    return render(request, 'apps/emp_Interface.html')

def emp_changePassword(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user 
    if request.method == "POST":
        current = request.POST['currentPassword']   
        new = request.POST['newPassword']  

        try:
            if user.check_password(current):
                user.set_password(new)
                user.save()
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"            
    return render(request, 'apps/emp_changePassword.html',locals())