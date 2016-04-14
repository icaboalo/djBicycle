from django.db import models
from utils.choices import *



# Create your models here.
class Bicycle(models.Model):
    class Meta:
        verbose_name = 'Bicycle'
        verbose_name_plural = 'Bicycles'

    #Attributes
    brand = models.CharField(max_length=50, blank=False)
    model = models.CharField(max_length=50, blank=False)
    track = models.CharField(max_length=4, choices=TRACK_CHOICES, blank=False)
    color = models.CharField(max_length=10, blank=False)
    year = models.CharField(max_length=4, choices=YEAR_CHOICES, blank=True)

    #--Geolocation
    latitude = models.CharField(max_digits=10, decimal_places=5, blank=True)
    longitude = models.CharField(max_digits=10, decimal_places=5, blank=True)


    def __str__(self):
        return self.brand + ' ' + self.model