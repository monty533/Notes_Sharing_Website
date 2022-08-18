from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib.auth import logout , authenticate , login
from django.contrib import messages
from .models import Destination
# Create your views here.
def index_view(request):

    dests = Destination.objects.all()
    
    return render(request, 'index.html', {'dests': dests})

def about_view(request):
    return render(request,'about.html')

def cities_view(request):
    return render(request,'cities.html')

def register_view(request):
    if request.method=='POST':
        f = request.POST['first_name']
        l = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        p1 = request.POST['password1']
        p2 = request.POST['password2']

        if p1==p2:
            if User.objects.filter(username=username).exists():
                # print('username taken')
                messages.info(request,'username taken')
                return redirect('Register')

            elif User.objects.filter(email=email).exists():
                # print('email taken')
                messages.info(request,'email taken')
                return redirect('Register')


            else:
                user = User.objects.create_user(username=username, email=email,first_name=f,last_name=l,password=p1)
                user.save()
                print('user created')
                return redirect('Login')
        else:
            messages.success(request,'password not matching')
            return redirect('Register')

        return redirect('/')

    else:
        return render(request, 'register.html')

def login_view(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credential')
            return redirect('Login')
    else:   
        return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')