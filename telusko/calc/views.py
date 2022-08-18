from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def add(request):
    val1 = request.POST['num1']
    val2 = request.POST['num2']
    val3 = int(val1) + int(val2)
    return render(request, 'result.html',{'result': val3})