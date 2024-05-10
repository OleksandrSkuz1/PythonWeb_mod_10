from django.shortcuts import render
from django.views import View

from .forms import RegisterForm

# Create your views here.


class RegisterView(View):
    template_name = 'app_auth/register.html'
    form_class = RegisterForm

    def get(self, request):
        return render(request, self.template_name, conte)

    def post(self, request):
        pass