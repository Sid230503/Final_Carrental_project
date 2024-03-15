from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('tenant-register/', views.TenantRegisterView.as_view(), name = "tenant-register"),
     
]
