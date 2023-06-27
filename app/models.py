
# Create your models here.
from django.db import models
from datetime import datetime


# Create your models here.

class MovieDataBase(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/")
    movie = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    createdat = models.DateTimeField(default=datetime.now)
    language = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)
    quality = models.CharField(max_length=255)
