from django.shortcuts import render
from .cart import Cart 
from store.models import Product, Category
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
# Create your views here.

def cart_summary(request):

    cart = Cart(request)

    return render(request, 'cart/cart_summary.html', {'cart':cart})

def cart_add(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        product_quantity = int(request.POST.get('product_quantity'))
        product = get_object_or_404(Product, id=product_id)
        
        cart.add(product=product, product_qty=product_quantity)
        response = JsonResponse({
            'qty': cart.count()
        })
        return response 
    
def cart_delete(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        cart.delete(product_id=product_id)
        
        response = JsonResponse({
            'qty': cart.count(),
            'total':cart.get_total()
        })

    return response 

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        cart.update()
