from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
from .forms import LoginForm

app_name = 'app_auth'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', LoginView.as_view(template_name='app_auth/signin.html', form_class=LoginForm), name='signin'),
    path('logout/', views.logout_view, name='logout'),  # Змінено
]

