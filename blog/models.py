from django.db import models

# Create your models here.


class PostModel(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.title}'


class CommetModel(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    body = models.TextField()
    is_validate = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.body[:50]}'
