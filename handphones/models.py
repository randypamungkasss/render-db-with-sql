from django.db import models

# Create your models here.
class Handphone(models.Model):
    brand = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    internal = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    battery = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.brand} {self.type}"
    
    