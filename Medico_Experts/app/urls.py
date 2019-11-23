"""Medico_Experts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name="index"),
    path('registration-page/',views.registration_page,name="registration-page"),
    path('login-page/',views.login_page,name="login-page"),
    path('register-user/',views.register_user,name="register-user"),

    path('login-evalute/',views.login_evalute,name="login-evalute"),
    path('Doctor-Dashboard/',views.Doctor_Dashboard,name="Doctor-Dashboard"),
   # path('patient-dashboard/',views.doctor_dashboard,name="doctor-dashboard"),
    
    path('logout/',views.logout,name="logout"),
    path('forgot-password-page/',views.forgot_password_page,name="forgot-password-page"),

    path('forgot-password/',views.forgot_password,name="forgot-password"),

    path('reset-password/',views.reset_password,name="reset-password"),

]

