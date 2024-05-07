from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, template_name='quotes_by_great_authors/index.html', context={'msg': 'Hello Alex!'})

def authors(request):
    return render(request, template_name='quotes_by_great_authors/authors.html', context={})

def quotes(request):
    return render(request, template_name='quotes_by_great_authors/quotes.html', context={})

def upload(request):
    return render(request, template_name='quotes_by_great_authors/upload.html', context={})
