from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
# Create your views here.


def index_view(request):
    if not request.user.is_staff:
        return redirect('Adminlogin')
    enquiry = Enquiry.objects.all()
    equipment = Equipment.objects.all()
    plan = Plan.objects.all()
    member = Member.objects.all()
    e1 = 0
    eq1 = 0
    p1 = 0
    m1 = 0
    for i in enquiry:
        e1 += 1
    for i in equipment:
        eq1 += 1
    for i in plan:
        p1 += 1
    for i in member:
        m1 += 1 

    d = {'e1': e1,'eq1':eq1,'p1':p1,'m1':m1}
    return render(request, 'index.html', d)


def about_view(request):
    return render(request, 'about.html')


def contact_view(request):
    return render(request, 'contact.html')


def adminlogin_view(request):
    error = ''
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = 'no'
            else:
                error = 'yes'
        except:
            error = 'yes'
    d = {'error': error}
    return render(request, 'adminlogin.html', d)


def logout_view(request):
    if not request.user.is_staff:
        return redirect('Adminlogin')
    logout(request)
    return redirect('Adminlogin')


def addenquiry_view(request):
    error = ''
    if not request.user.is_staff:
        return redirect('Adminlogin')

    if request.method == 'POST':
        n = request.POST['name']
        c = request.POST['contact']
        e = request.POST['email']
        a = request.POST['age']
        g = request.POST['gender']
        try:
            Enquiry.objects.create(name=n, contact=c, emailid=e, age=a, gender=g)
            error = 'no'
        except:
            error = 'yes'
    d =  {'error':error}
    return render(request,'addenquiry.html',d)

def viewenquiry_view(request):

    if not request.user.is_staff:
        return redirect('Adminlogin')
    enq = Enquiry.objects.all()
    d =  {'enq':enq}
    return render(request,'viewenquiry.html',d)

def Delete_Enquiry_view(request,pid):

    if not request.user.is_staff:
        return redirect('Adminlogin')
    enquiry = Enquiry.objects.get(id=pid)
    enquiry.delete()
    return redirect('Viewenquiry')


def addequipment_view(request):
    error = ''
    if not request.user.is_staff:
        return redirect('Adminlogin')

    if request.method == 'POST':
        n = request.POST['name']
        p = request.POST['price']
        u = request.POST['unit']
        d = request.POST['date']
        de = request.POST['desc']
        try:
            Equipment.objects.create(name=n, price=p, unit=u, date=d, desc=de)
            error = 'no'
        except:
            error = 'yes'
    d =  {'error':error}
    return render(request,'addequipment.html',d)

def viewequipment_view(request):

    if not request.user.is_staff:
        return redirect('Adminlogin')
    equip = Equipment.objects.all()
    d =  {'equip':equip}
    return render(request,'viewequipment.html',d)

def delete_equipment_view(request,pid):

    if not request.user.is_staff:
        return redirect('Adminlogin')
    equipment = Equipment.objects.get(id=pid)
    equipment.delete()
    return redirect('Viewequipment')


def add_plan_view(request):
    error = ''
    if not request.user.is_staff:
        return redirect('Adminlogin')

    if request.method == 'POST':
        n = request.POST['name']
        a = request.POST['amount']
        d = request.POST['duration']
        
        try:
            Plan.objects.create(name=n, amount=a, duration=d)
            error = 'no'
        except:
            error = 'yes'
    d =  {'error':error}
    return render(request,'add_plan.html',d)

def view_plan_view(request):

    if not request.user.is_staff:
        return redirect('Adminlogin')
    plan = Plan.objects.all()
    d =  {'plan':plan}
    return render(request,'view_plan.html',d)

def delete_plan_view(request,pid):

    if not request.user.is_staff:
        return redirect('Adminlogin')
    plan = Plan.objects.get(id=pid)
    plan.delete()
    return redirect('View_plan')


def add_member_view(request):
    error = ''
    if not request.user.is_staff:
        return redirect('Adminlogin')

    plan1 = Plan.objects.all()

    if request.method == 'POST':
        n = request.POST['name']
        c = request.POST['contact']
        e = request.POST['email']
        a = request.POST['age']
        g = request.POST['gender']
        p = request.POST['plan']
        j = request.POST['joindate']
        ex = request.POST['expiredate']
        am = request.POST['initialamount']
        plan = Plan.objects.filter(name=p).first()
        try:
            Member.objects.create(name=n, contact=c, emailid=e, age=a, gender=g,plan=plan,joindate=j,expiredate=ex,initialamount=am)
            error = 'no'
        except:
            error = 'yes'
    d =  {'error':error,'plan':plan1}
    return render(request,'add_member.html',d)

def view_member_view(request):

    if not request.user.is_staff:
        return redirect('Adminlogin')
    member = Member.objects.all()
    d =  {'member':member}
    return render(request,'view_member.html',d)

def delete_member_view(request,pid):

    if not request.user.is_staff:
        return redirect('Adminlogin')
    member = Member.objects.get(id=pid)
    member.delete()
    return redirect('View_member')
