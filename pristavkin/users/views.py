from django.shortcuts import render
from .forms import CreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
# Create your views here.


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('shop:home')
    template_name = 'users/signup.html'

def test(request):
    return render(request,'users/login.html')