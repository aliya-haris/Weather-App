from django.db import models

# Create your models here.
class Weather(models.Model):
    city = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10)
    coordinate = models.CharField(max_length=10)
    temp = models.DecimalField(max_digits=20, decimal_places=3)
    pressure = models.DecimalField(max_digits=10, decimal_places=3)
    humidity = models.DecimalField(max_digits=10, decimal_places=3)
    timestamp = models.DateTimeField(auto_now_add=True)

