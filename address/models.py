# address/models.py

from django.db import models
from apps.userprofile.models import Profile

class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    address_line = models.CharField(max_length=255) 
    profile = models.ForeignKey(Profile, related_name='addresses', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"{self.address_line}, {self.city}, {self.state}, {self.country} - {self.postal_code}"
