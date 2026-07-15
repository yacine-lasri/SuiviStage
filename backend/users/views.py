from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('login')

class CustomLoginView(LoginView):
    template_name = 'users/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')
