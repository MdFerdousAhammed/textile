from django.db import models

from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    details = models.TextField()
    image = models.ImageField(default="default.jpg", upload_to = 'img')
    posted_at = models.DateTimeField(default=now)


    def __str__(self):
        return self.name


# api

class Postai(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)  
    image = models.ImageField(default="default.jpg" ,upload_to ='potos')
    def __str__(self):
        return self.title


