from django.shortcuts import render
from store.models import Product, Category
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse

def register(request):
    
    return render(request, 'account/registration/register.html')