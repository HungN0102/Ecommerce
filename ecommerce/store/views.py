from django.shortcuts import render, get_object_or_404
from .models import Product, Category

# Create your views here.
def store(request):
    all_products = Product.objects.all()
    context_dict = {
        'my_products': all_products
    }
    return render(request, 'store/store.html', context_dict)

def categories(request):
    all_categories = Category.objects.all()
    return {'all_categories': all_categories}

def product_info(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product 
    }
    
    return render(request, 'store/product_info.html', context)

def list_category(request, slug=None):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    
    return render(request, 'store/list_category.html',{
        'category': category,
        'products': products
    })
