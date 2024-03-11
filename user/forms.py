from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.db import transaction

class TenantRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','email','password','age','is_tenant']
    
    @transaction.atomic
    def save(self):
        