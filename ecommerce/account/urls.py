from django.urls import path 
from . import views 

urlpatterns = [
    path('register', views.register, name='register'),
    
    # email verification urls 
    path('email_verification<str:uidb64>/<str:token>', views.register, name='email_verification'),
    path('email_verification_sent', views.email_verification_sent, name='email_verification_sent'),
    path('email_verification_success', views.register, name='email_verification_successs'),
    path('email_verification_failed', views.register, name='email_verification_failed'),
]
