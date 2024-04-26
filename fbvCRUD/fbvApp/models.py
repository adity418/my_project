from django.db import models

# Create your models here.
class Student(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    topScore = models.FloatField()