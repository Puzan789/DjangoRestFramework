from django.db import models

# Create your models here.
class students(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    cp=models.CharField(max_length=100)
