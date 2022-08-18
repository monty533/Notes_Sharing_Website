from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,logout,login

# Create your views here.
def index_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def userlogin_view(request):
    error = ''
    if request.method=="POST":
        e = request.POST['email']
        p = request.POST['password']
        user = authenticate(email=e, password=p)
        print("user ",user)
        
        try:
            if user:
                print("user 1",user)

                login(request, user)
                error = 'no'
            else:
                print("user 2",user)

                error = 'yes'
        except:
            error = 'yes'
        
    d = {'error': error}
    return render(request, 'login.html',d)

def adminlogin_view(request):
    error = ''
    if request.method=="POST":
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        try:
            if request.user.is_staff:
                login(request, user)
                error = 'no'
            else:
                error = 'yes'
        except:
            error = 'yes'
        
    d = {'error': error}
    return render(request, 'adminlogin.html',d)

def signup_view(request):
    error = ''
    if request.method == 'POST':
        f = request.POST['firstname']
        l = request.POST['lastname']
        c = request.POST['contact']
        e = request.POST['emailid']
        ps = request.POST['password']
        b = request.POST['branch']
        r = request.POST['role']
        try:
            print('nitin')
            user = User.objects.create_user(username=e,password=ps,firstname=f,lastname=l)
            print('nitin ',user)

            Signup.objects.create(user=user,contact=c,branch=b,role=r)
            
            error = 'no'
        except:
            error = 'yes'
    d = {'error':error}        
    return render(request, 'signup.html',d)


def adminhome_view(request):
    if not request.user.is_staff:
        return redirect('/adminlogin')
    return render(request, 'adminhome.html')

def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('/userlogin')
    user = User.objects.get(id=request.user.id)
    data = Signup.objects.get(user=user)
    d = {'data':data,'user':user}
    return render(request, 'profile.html',d)
