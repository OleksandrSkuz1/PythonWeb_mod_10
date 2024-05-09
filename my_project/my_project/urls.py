from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quotes_by_great_authors.urls')),
   # path('users/', include('users.urls'))
]
