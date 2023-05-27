from django.urls import path 
from . import views 
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('register', views.register, name='register'),
    
    # email verification urls 
    path('email-verification<str:uidb64>/<str:token>', views.email_verification, name='email_verification'),
    path('email-verification-sent', views.email_verification_sent, name='email_verification_sent'),
    path('email-verification-success', views.email_verification_success, name='email_verification_success'),
    path('email-verification-failed', views.email_verification_failed, name='email_verification_failed'),
    
    # login
    path('my-login', views.my_login, name='my_login'),
    
    # logout
    path('my-logout', views.user_logout, name='user_logout'),
    
    # dashboard
    path('', views.dashboard, name='dashboard'),
    
    # management
    path('track-orders', views.track_orders, name='track_orders'),
    path('profile-management', views.profile_management, name='profile_management'),
    path('manage-shipping', views.manage_shipping, name='manage_shipping'),
    path('delete-account', views.delete_account, name='delete_account'),
    
    # password management views
    path('reset-password', auth_views.PasswordResetView.as_view(template_name='account/password/password_reset.html'), name='reset_password'), #submit our email form
    path('reset-password-sent', auth_views.PasswordResetDoneView.as_view(template_name='account/password/password_reset_sent.html'), name='reset_password_done'), #submit our email form
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='account/password/password_reset_form.html'), name='password_reset_confirm'),
    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password/password_reset_complete.html'), name='password_reset_complete'),
    
]
