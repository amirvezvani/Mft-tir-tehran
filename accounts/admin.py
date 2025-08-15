from django.contrib import admin
from .models import UserProfileModel,AddEducationModel,AddExperienceModel
# Register your models here.
m=[UserProfileModel,AddEducationModel,AddExperienceModel]
admin.site.register(m)
