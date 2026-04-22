from django.contrib import admin
from django.urls import path
from clinicavet.views import animals, appointments, clientes


urlpatterns = [
    path('admin/', admin.site.urls),
    path('animais/', animals, name='animais'),
    path('clientes/', clientes, name='clientes'),
    path('agendamento/', appointments, name='agendamento'),
]
