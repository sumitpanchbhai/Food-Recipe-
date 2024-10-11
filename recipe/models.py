from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    recipe_desciption =  models.CharField(max_length=100000)
    recipe_image = models.ImageField(upload_to='recipe_images/')