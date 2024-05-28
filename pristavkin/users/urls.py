
from . import views

from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView, \
    PasswordResetConfirmView, PasswordChangeView, PasswordChangeDoneView, LogoutView
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
    path(
        'auth/logout/',
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout'
    ),
    path(
        'auth/password_reset/',
        PasswordResetView.as_view(
            template_name='users/managment/password_reset_form.html',
            email_template_name='users/managment/password_reset_email.html',
            success_url='done/'),
        name='password_reset_form'
    ),

    path('auth/password_reset/done/',
         PasswordResetDoneView.as_view(
             template_name='users/managment/password_reset_done.html'),
         name='password_reset_done'),

    path('auth/reset/done/',
         PasswordResetCompleteView.as_view(
             template_name='users/managment/reset_done.html'),
         name='reset_done'),

    path('auth/password_reset_confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='users/managment/password_reset_confirm.html',
             success_url=reverse_lazy('users:reset_done')),
         name='password_reset_confirm'),

    path(
        'auth/password_reset_complete/',
        PasswordResetCompleteView.as_view(
            template_name='users/managment/password_reset_complete.html'),
        name='password_reset_complete'
    ),

    path(
        'auth/password_change/',
        PasswordChangeView.as_view(
            template_name='users/managment/password_change_form.html',
            success_url='done/'),
        name='password_change'
    ),
    path(
        'auth/password_change/done/',
        PasswordChangeDoneView.as_view(
            template_name='users/managment/password_change_done.html'),
        name='password_change_done'
    ),
]
