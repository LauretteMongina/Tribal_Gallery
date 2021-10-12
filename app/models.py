from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
    
    def update_category(self, update):
        self.name = update
        self.save()

class Location(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def save_location(self):
        self.save()

    def update_location(self, name):
        self.name = name
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name
class Image(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self,name, description , location, category):
        self.name = name
        self.description = description
        self.location = location
        self.category = category
        self.save()

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls, id):
        image = Image.objects.filter(id=id).all()
        return image
    
    @classmethod
    def filter_by_category(cls,category):
        images = Image.objects.filter(category__name=category)
        return images
    @classmethod
    def filter_by_location(cls,location):

        images = Image.objects.filter(location__name=location)
        return images
    
    @classmethod
    def search_image(cls, search_term):
        images = cls.objects.filter(name__icontains=search_term)
        return images
    def __str__(self):
        return self.name

