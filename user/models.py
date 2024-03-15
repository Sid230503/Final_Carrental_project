from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_renter = models.BooleanField(default=False)
    is_tenant = models.BooleanField(default=False)
    driver_license_number = models.CharField(max_length=50, null=True, blank=True)
    renter_license_number = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.username
    

    class meta:
        db_table = 'user'