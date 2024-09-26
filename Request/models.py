from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Trade4me(models.Model):
    full_name = models.CharField(max_length=200)
    email =     models.CharField(max_length=200)
    login_ID =  models.CharField(max_length=200)
    password =   models.CharField(max_length=200) 

    def __str__(self):
        return self.full_name













   
    
"""
class CustomerDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='customer')
    PhoneNumber = models.IntegerField()
    Address = models.CharField(max_length=100)
    Age = models.IntegerField()
    State = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.user.First_name}"
    """