from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    Age = models.PositiveBigIntegerField(null=True,blank =True)
    is_renter = models.BooleanField(default=False)
    is_tenant = models.BooleanField(default=False)
    driver_license_number = models.CharField(max_length=50, null=True, blank=True)
    renter_license_number = models.CharField(max_length=50, null=True, blank=True)
   

    class meta:
        db_table = 'user'