from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    instructor = models.CharField(max_length=50)
    rating = models.FloatField()