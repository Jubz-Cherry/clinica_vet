from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=30)
    race = models.CharField(max_length=30)
    age =  models.CharField(max_length=10)
    birth = models.DateField(max_length=14)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Owner(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    telephone = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
    description = models.TextField(max_length=500)
   