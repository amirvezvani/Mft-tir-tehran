from django.db import models
from django.urls import reverse
from accounts.models import UserProfileModel
from django.utils.text import slugify
# Create your models here.


class PostModel(models.Model):
    author=models.ForeignKey(UserProfileModel,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    like=models.ManyToManyField(UserProfileModel,related_name='user_like',null=True,blank=True)
    dislike=models.ManyToManyField(UserProfileModel,related_name='user_dislike',null=True,blank=True)
    slug=models.SlugField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return f'{self.title}'

    def save(self):
        super().save()
        if not self.slug:
            self.slug=slugify(self.title)
            self.save()

    def get_absolute_url(self):
        return reverse("post", kwargs={"slug": self.slug})
    

class CommetModel(models.Model):
    author=models.ForeignKey(UserProfileModel,on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    body = models.TextField()
    is_validate = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.body[:50]}'
