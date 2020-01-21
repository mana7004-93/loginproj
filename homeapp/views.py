from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from homeapp.forms import SignUpFrom
# Create your views here.
def Home_page(request):
    return render(request,'home.html')
def Customer(request):
    return render(request,'customer.html')
def Logout_Views(request):
    return render(request,'logout.html')
def Registration_View(request):
    form=SignUpFrom()
    return render(request, 'register.html',{'form':form})