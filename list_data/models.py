from django.db import models

# Create your models here.
class ListData(models.Model):
    list_image = models.FileField()
    likes = models.IntegerField()
    comments = models.IntegerField()
    shares = models.IntegerField()
