from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        var=request.POST['username']
        var2=request.POST['password']
        var3=auth.authenticate(username=var,password=var2)

        if var3 is not None:
            auth.login(request,var3)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return render(request,'login.html')



    return render(request,'login.html')


def register(request):
    if request.method=='POST':
        a = request.POST['username']
        b = request.POST['first name']
        f = request.POST['last name']
        c = request.POST['email']
        d = request.POST['password']
        e = request.POST['password1']
        if d==e:
            if User.objects.filter(username=a).exists():
                messages.info(request,'username already exist')
                return redirect('register')
            elif User.objects.filter(email=c).exists():
                messages.info(request,'email already exist')
                return redirect('register')
            else:

                var=User.objects.create_user(username=a,password=d,first_name=b,last_name=f,email=c)
                var.save();

                return redirect('login')
        else:
            messages.info(request,'incorrect password')
            return redirect('register')


    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
