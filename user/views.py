from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic.edit import CreateView
from user.forms import TenantRegistrationForm, RenterRegistrationForm
from user.models import User
from crispy_forms.utils import render_crispy_form

# Create your views here.
class TenantRegisterView(CreateView):
    template_name = 'user/tenanat_register.html'
    model =  User
    form_class = TenantRegistrationForm
    success_url = "/login/"

    
class RenterRegisterView(CreateView):
    template_name = 'user/renter_register.html'
    model =  User
    form_class = RenterRegistrationForm
    success_url = "/login/"

