from django.db import models
from datetime import date
  
class Dni(models.Model):
  dni = models.CharField(max_length=10, blank=False, null=False)

  def __str__(self):
      return self.dni

class Person(models.Model,date):
  first_name = models.CharField(max_length=15, blank=False, null=False)
  last_name= models.CharField(max_length=15, blank=False, null=False)
  date = models.DateField(max_length=10, blank=False, null=False)
  email= models.EmailField(max_length=75, blank=False, null=False)
  dni = models.ForeignKey(Dni, on_delete=models.CASCADE, related_name='People')

  def __str__(self):
      return self.first_name

