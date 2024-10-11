from django.db import models

# Create your models here.
class Student(models.Model):  # Corrected from models.model to models.Model
    first_name = models.CharField(max_length=20)
    age = models.IntegerField()  # Removed max_length, IntegerField doesn't use it
    last_name = models.CharField(max_length=20)
    class_rank = models.IntegerField()  # Removed max_length

