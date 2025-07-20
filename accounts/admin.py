from django.contrib import admin
from .models import UserProfile
# Register your models here.
m=[UserProfile]
admin.site.register(m)
