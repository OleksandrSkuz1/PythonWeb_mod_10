from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.

class RegisterView(View):
    template_name = 'app_auth/signup.html'
    form_class = RegisterForm