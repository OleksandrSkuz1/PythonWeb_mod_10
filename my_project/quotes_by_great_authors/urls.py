from django.urls import path, include

from . import views

app_name = "quotes_by_great_authors"

urlpatterns = [
    path('', views.index, name='home'),  # quotes_by_great_authors:home
    path('authors/', views.authors, name='authors'),
    path('quotes/', views.quotes, name='quotes'),
    path('upload/', views.upload, name='upload')
]