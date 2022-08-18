from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate, logout

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        return render(request, 'index.html')


def loginu(request):
    if request.method=='POST':
        u = request.POST['username']
        p = request.POST['password']
        print(u,p)
        user = authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render(request,'login.html')

    return render(request, 'login.html')
    

def logoutu(request):
    logout(request)
    return redirect('login')
    

