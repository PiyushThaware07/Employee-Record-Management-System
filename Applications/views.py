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

def emp_logout(request):
    logout(request)
    return redirect('index')

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

def emp_Interface(request):
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