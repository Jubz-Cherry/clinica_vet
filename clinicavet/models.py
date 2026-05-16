from django.db import models

class Cliente(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False)
    telephone = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Animal(models.Model):

    STATUS_CHOICES = [
        ('urgent', 'Urgent'),
        ('normal', 'Normal'),
        ('low', 'Low'),
    ]
     
    animal_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=30)
    specie = models.CharField(max_length=30)
    race = models.CharField(max_length=30)
    age = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='normal'
    )

    def __str__(self):
        return self.animal_name


class Appointment(models.Model):

    APPOINTMENT_STATUS = [
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('missed', 'Missed'),
        ('cancelled', 'Cancelled'),
    ]

    PRIORITY_STATUS = [
        ('urgent', 'Urgent'),
        ('normal', 'Normal'),
        ('low', 'Low'),  
    ]

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    date = models.DateField()
    hour = models.TimeField()
    description = models.CharField(max_length=100)

    status = models.CharField(
        max_length=20,
        choices=APPOINTMENT_STATUS,
        default='scheduled'
    )
    
    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_STATUS,
        default='normal'
    )


    def __str__(self):
        return f"{self.animal.animal_name} - {self.date}"