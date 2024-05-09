from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'quotes_by_great_authors/index.html', context={})

#def quotes(request):
 #   return render(request, template_name='quotes_by_great_authors/quotes.html', context={})

#def upload(request):
 #   return render(request, template_name='quotes_by_great_authors/upload.html', context={})
