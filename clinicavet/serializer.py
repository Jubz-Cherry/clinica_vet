from rest_framework import serializers
from clinicavet.models import Cliente, Animal, Appointment


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'id',
            'name',
            'email',
            'telephone',
        ]


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = [
            'id',
            'animal_name',
            'gender',
            'specie',
            'race',
            'age',
            'cliente',
        ]

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = [
            'id',
            'animal',
            'date',
            'hour',
            'description',
            'status',
        ]