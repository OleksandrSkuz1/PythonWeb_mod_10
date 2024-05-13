from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import login
from .forms import RegisterForm

def logout_view(request):
    if request.method == 'POST':  # Змінено на POST
        logout(request)
        return redirect('app_auth:signin')
    else:
        return render(request, 'app_auth/logout.html')  # Додано для GET запитів

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('quotes_by_great_authors:root')
    else:
        form = RegisterForm()
    return render(request, 'app_auth/signup.html', {'form': form})

