from django.contrib import admin
from django.urls import path
from clinicavet.views import animals
from clinicavet.views import donos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('animals/', animals, name='animals'),
    path('donos/', donos, name='donos'),
]
