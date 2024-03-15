from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.db import transaction

class TenantRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','email','password1','password2','is_tenant']
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_tenant = True
        user.save()
        return user


class RenterRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','email','password1','password2','is_renter']
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_renter = True
        user.save()
        return user