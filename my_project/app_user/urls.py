from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = "quotes_by_great_authors"

urlpatterns = [
    path('signup/', views.index, name='home'),  # quotes_by_great_authors:home
    path('signin/', LoginView.as_view(), name='signin'),
    path('logout/', LogoutView.as_view(), name='logout'),

]