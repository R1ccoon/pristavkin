from .views import *
from django.contrib import admin
from django.urls import path, include
app_name = 'users'

urlpatterns = [
    path('auth/signup/', SignUp.as_view(), name='signup'),

]
