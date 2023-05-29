# for general
from django.shortcuts import render, redirect 

# for login
from django.contrib.auth.models import auth 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# for importing models 
from .models import ShippingAddress

# for importing forms
from .forms import ShippingForm


# Create your views here.

def checkout(request):
    form = ShippingForm()
    if request.user.is_authenticated:
        try:
            shipping_address = ShippingAddress.objects.get(user=request.user)
            form = ShippingForm(instance=shipping_address)
            return render(request, 'payment/checkout.html', {'form': form})
        except:
            return render(request, 'payment/checkout.html', {'form': form})
            
    return render(request, 'payment/checkout.html', context={'form': form})

def payment_success(request):
    
    return render(request, 'payment/payment_success.html')

def payment_failed(request):
    
    return render(request, 'payment/payment_failed.html')

