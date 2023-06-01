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

# import json
from django.http import JsonResponse

# Create your views here.

def checkout(request):
    if request.user.is_authenticated:
        try:
            shipping_address = ShippingAddress.objects.get(user=request.user)
            return render(request, 'payment/checkout.html', {'shipping': shipping_address})
        except:
            return render(request, 'payment/checkout.html')
    return render(request, 'payment/checkout.html')

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
        
        """
        Create Order For
        
        1) Account Users (With or Without shipping information)
        
        2) Guest Users
        """
        
        # 1) Account Users (With or Without shipping information)
        if request.user.is_authenticated:
            order = Order.objects.create(
                full_name=name,
                email=email,
                shipping_address=shipping_address,
                amount_paid=total_cost,
                user=request.user
            )
            

            for item in cart:
                OrderItem.objects.create(
                        quantity = item['qty'],
                        price = item['price'],
                        
                        # FK
                        user = request.user,
                        order = order,
                        product = item['product']
                    )
        
        # 2) Guest Users
        else:
            order = Order.objects.create(
                full_name=name,
                email=email,
                shipping_address=shipping_address,
                amount_paid=total_cost
            )
            
            for item in cart:
                OrderItem.objects.create(
                        quantity = item['qty'],
                        price = item['price'],
                        
                        # FK
                        order = order,
                        product = item['product']
                    )

        order_success = True 
        response = JsonResponse({
            'success': order_success
        })
        
        return response
        
def payment_success(request):
    cart = Cart(request)
    for key in list(request.session.keys()):
        if key == 'session_key':
            del request.session[key]
    return render(request, 'payment/payment_success.html')

def payment_failed(request):
    
    return render(request, 'payment/payment_failed.html')

