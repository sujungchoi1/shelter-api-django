from django.db import models

# Create your models here.
class Shelter(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    service = models.CharField(max_length=60, null=True, blank=True)
    hours = models.CharField(max_length=60, null=True, blank=True)
    contact = models.CharField(max_length=60, null=True, blank=True)
    
    def __str__(self):
        return self.name