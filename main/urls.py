from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('predict/', views.predict_view, name='predict'),  # ✅ this one only

    #New OTP URLs
    path('otp/', views.otp_request_view, name='otp'),
    path('otp-verify/',views.otp_verify_view, name='otp_verify'),
    path('resend-otp/', views.resend_otp, name='resend_otp'),

    #Admin Paths
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('adminlogout/', views.adminlogout, name='adminlogout'),


]

