from django.contrib import admin
from .models import PostModel,CommetModel

# Register your models here.
m=[PostModel,CommetModel]
admin.site.register(m)