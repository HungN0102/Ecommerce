from django.urls import path 
from . import views 

urlpatterns = [
    path('checkout', views.checkout, name='checkout'),
    
    path('payment-success', views.payment_success, name='payment_success'),
    path('payment-failed', views.payment_failed, name='payment_failed'),
    path('complete-order', views.complete_order, name='complete_order'),
]

