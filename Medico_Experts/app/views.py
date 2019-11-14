from django.shortcuts import render
from .models import *
import time

# Create your views here.
def index(request):
    if 'email' in request.session:
        return render(request,"app/dashboard/index.html")
    else:
        return render(request,"app/authentication/login.html")

def registration_page(request):
    return render(request,"app/authentication/register.html")

def login_page(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        did=Doctor.objects.get(user_id=uid)
        return render(request,"app/dashboard/Base_Doctor.html",{'did':did})
    else:
        return render(request,"app/authentication/login.html")

def register_user(request):
    try:
        role=request.POST['role']
        firstname=request.POST['firstname']
        email=request.POST['email']
        password=request.POST['password']
        terms=request.POST['terms']
        
        uid=User.objects.filter(email=email)
 
        if uid:
            e_msg="User Already Exist"
            return render(request,"app/authentication/register.html",{'e_msg':e_msg})

        else:
            user_id=User.objects.create(role=role,email=email,password=password)
            if role=="Doctor":
                if user_id:
                    did=Doctor.objects.create(user_id=user_id,firstname=firstname)
                    if did:
                        s_msg="Success : Registration successfully"
                        return render(request,"app/authentication/register.html",{'s_msg':s_msg})
                    else:
                        e_msg="Error : Invalid value"
                        return render(request,"app/authentication/register.html",{'e_msg':e_msg})
                else:
                    e_msg="Error : Invalid email and password"
                    return render(request,"app/authentication/register.html",{'e_msg':e_msg})
            else:
                if user_id:
                    pid=Patient.objects.create(user_id=user_id,firstname=firstname)
                    if pid:
                        s_msg="Success : Registration successfully"
                        return render(request,"app/authentication/register.html",{'s_msg':s_msg})
                    else:
                        e_msg="Error : Invalid value"
                        return render(request,"app/authentication/register.html",{'e_msg':e_msg})
                else:
                    e_msg="Error : Invalid email and password"
                    return render(request,"app/authentication/register.html",{'e_msg':e_msg})
    except:
        e_msg="Error : Enter Require Fields "
        return render(request,"app/authentication/register.html",{'e_msg':e_msg})

def login_evalute(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        role=uid.role
        if role=="Doctor":
            did=Doctor.objects.get(user_id=uid)
            print("_______>",uid)
            return render(request,"app/dashboard/Base_Doctor.html",{'did':did})
        else:
            pid=Patient.objects.get(user_id=uid)
            return render(request,"app/dashboard/Base_Patient.html",{'pid':pid})
    else:
        try:
            role=request.POST['role']
            email=request.POST['email']
            password=request.POST['password']
            uid=User.objects.get(email=email)
            print("--------------->role",role)
            if uid.email==email and uid.password==password:
                if role=='Doctor':
                    did=Doctor.objects.get(user_id=uid)
                    request.session['id']=did.id
                    request.session['email']=uid.email                
                    print("----------------> profile pic",did.profile_pic.url)
                    return render(request,"app/dashboard/Base_Doctor.html",{'did':did})
                if role=='Patient':
                    pid=Patient.objects.get(user_id=uid)
                    request.session['id']=pid.id
                    request.session['email']=uid.email
                    print("------------------>pid",pid)
                    return render(request,"app/dashboard/Base_Patient.html",{'pid':pid})
            else:
                e_msg="Error : Invalid email and password"
                return render(request,"app/authentication/login.html",{'e_msg':e_msg})
        except:
            e_msg="Error : Invalid email and password"
            return render(request,"app/authentication/login.html",{'e_msg':e_msg})

def Doctor_Dashboard(request):
    return render(request,"app/dashboard/Base_Doctor.html")
    

def logout(request):
    if "email" in request.session:
        del request.session['id']
        del request.session['email']
        return render(request,"app/authentication/login.html")
    else:
        return render(request,"app/authentication/login.html")
        
    
    
    
