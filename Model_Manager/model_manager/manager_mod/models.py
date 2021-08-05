from django.db import models

# Create your models here.

class modmanager(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.TextField()
    morelation = models.Manager()




