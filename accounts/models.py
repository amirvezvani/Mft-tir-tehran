from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse
# Create your models here.

class UserProfileModel(models.Model):
    bio=models.CharField(max_length=100,default='bio for You')
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    picture=models.ImageField(upload_to='user_profile',default='user_profile/profile.png')
    
    def __str__(self):
        return self.bio
    
    def get_absolute_url(self):
        return reverse("profile", kwargs={"pk": self.pk})
    
    
class AddEducationModel(models.Model):
    school=models.CharField(max_length=25)
    degree=models.CharField(max_length=25)
    field=models.CharField(max_length=25)
    start= models.DateTimeField()
    end= models.DateTimeField(null=True,blank=True)
    description=models.TextField()
    
    def __str__(self):
        return self.school
    
    
class AddExperienceModel(models.Model):
    job=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    start= models.DateTimeField()
    end= models.DateTimeField(null=True,blank=True)
    description=models.TextField()
    
    def __str__(self):
        return self.job
    
    

@receiver(post_save, sender=User) 
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfileModel.objects.create(user=instance)