from django.db import models

# Create your models here.
class Employee(models.Model):

    id_e = models.CharField(max_length=100)

    address = models.CharField(max_length=200)

    name = models.CharField(max_length=300)

    position = models.CharField(max_length=200)

    start_year = models.IntegerField()

    total_attend = models.IntegerField()

    dob = models.CharField(max_length=1000)

    def __str__(self):
        return  self.name