from django.shortcuts import render
from .cart import Cart 
from store.models import Product, Category
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
# Create your views here.
def cart_summary(request):
    return render(request, 'cart/cart_summary.html', {})

def cart_add(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        product = get_object_or_404(Product, product_id)
        
        cart.add(product=product, product_qty=product_quantity)
        response = JsonResponse({
            'The product title is called: ': product.title,
            '  and the product quantity is:  ': product_quantity
        })
        return response 

def cart_delete(request):
    pass 

def cart_update(request):
    pass 
