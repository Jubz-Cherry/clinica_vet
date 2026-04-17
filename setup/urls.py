from django.contrib import admin
from django.urls import path
from clinicavet.views import animals

urlpatterns = [
    path('admin/', admin.site.urls),
    path('animals/', animals, name='animals'),
]
