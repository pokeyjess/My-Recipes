from django.db import models
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.models import CloudinaryField

# https://hackernoon.com/building-social-network-project-using-django-cloudinary-and-sendgrid-together-682t3ufe

cloudinary.config( 
  secure=True,
  cloud_name = 'hoiomsa7b', 
  api_key = '298816973249399', 
  api_secret = 'TB3nWo0kI1mcMBffm1EVFuf_jkY' 
)


class Category(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    summary = models.TextField()
    instructions = models.TextField()
    # recipe_image = models.ImageField(upload_to='images/', null=True, blank=True)
    recipe_image = CloudinaryField('image', null=True, blank=True, default="default_photo3.jpg")


    class Meta:
        ordering = ('title',)
    
    def __str__(self):
        return f"{self.title} : {self.category.name}"

