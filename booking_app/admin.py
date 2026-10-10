from django.contrib import admin
from django.urls import path, include
from .models import Booking, Apart

admin.site.register(Apart)
admin.site.register(Booking)