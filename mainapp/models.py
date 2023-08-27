from django.db import models
import random
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=50)
    capital = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name