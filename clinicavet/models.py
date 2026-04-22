from django.db import models

class Cliente(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False)
    telephone = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Animal(models.Model):
    animal_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=30)
    specie = models.CharField(max_length=30)
    race = models.CharField(max_length=30)
    age = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.animal_name


class Appointment(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    date = models.DateField()
    hour = models.TimeField()
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.animal.animal_name} - {self.date}"