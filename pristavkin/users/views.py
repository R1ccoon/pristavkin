from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import CreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Create your views here.


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'


@login_required
def profile(request):
    """
    Представление профиля пользователя.
    """
    return render(request, 'users/profile.html')
