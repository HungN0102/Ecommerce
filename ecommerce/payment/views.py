# for general
from django.shortcuts import render, redirect 

# for login
from django.contrib.auth.models import auth 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# for importing models 
from .models import ShippingAddress, Order, OrderItem
from cart.cart import Cart

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

def complete_order(request):
    if request.POST.get('action') == 'post':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        
        shipping_address = (
            address1 + '\n'+
            address2 + '\n'+
            city + '\n'+
            state + '\n'+
            zipcode + '\n'
        )
        
        # shopping carad information
        cart = Cart(request)
        total_cost = cart.get_total()
        
        
        
        if request.user.is_authenticated:
            order = Order.objects.create(
                full_name=name,
                email=email,
                shipping_address=shipping_address,
                amount_paid=total_cost,
                user=request.user
            )

def payment_success(request):
    
    return render(request, 'payment/payment_success.html')

def payment_failed(request):
    
    return render(request, 'payment/payment_failed.html')

