
from . import views

from django.contrib.auth.views import LoginView
from .views import *
from django.contrib import admin
from django.urls import path, include
app_name = 'users'

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('auth/signup/', SignUp.as_view(), name='signup'),
    path(
        'auth/login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),


]
