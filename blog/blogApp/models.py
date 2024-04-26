from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str___(self):
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=50)
    contents = models.TextField()
    created_by = models.CharField(max_length=50, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title 