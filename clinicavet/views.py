from clinicavet.models import Animal, Cliente, Appointment
from clinicavet.serializers import ClienteSerializer, AnimalSerializer, AppointmentSerializer  
from rest_framework import viewsets 


class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class AnimalsViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class AppointmentsViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

