from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class PointOfInterest(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='PointsOfInterest', default=True)
    location_name = models.TextField(max_length=50)
    notes = models.TextField(blank=True)
    street_address = models.CharField(verbose_name='Street Address', max_length=255)
    city = models.CharField(verbose_name='City', max_length=55)
    state = models.CharField(verbose_name='State', max_length=25)
    zip_code = models.CharField(verbose_name='Zip', max_length=5)
    images = models.ImageField(upload_to='media/images/', null=True)
    category = models.CharField(max_length=35)
    date_created = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.location_name}" 

class TellYourStory(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='TellYourStories', default=True)
    poi = models.ForeignKey(to=PointOfInterest, on_delete=models.CASCADE, related_name='TellYourStories', null=True)  
    text = models.TextField(max_length=255, null=True)
    images = models.ImageField(upload_to='media/images/', null=True, blank=True)
    date_created = models.DateField(auto_now=True)


    def __str__(self):
        return f"{self.poi} {self.date_created}"
