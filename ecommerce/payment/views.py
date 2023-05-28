# for general
from django.shortcuts import render, redirect 

# for login
from django.contrib.auth.models import auth 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def payment_success(request):
    
    return render(request, 'payment/payment_success.html')

def payment_failed(request):
    
    return render(request, 'payment/payment_failed.html')