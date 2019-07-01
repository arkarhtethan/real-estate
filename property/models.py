from django.db import models

import os
import datetime
# Create your models here.

def upload_path(instance, file_name):

    new_file_name = os.path.split(file_name)[1]

    prefix = str(datetime.datetime.now())

    return "-".join([prefix,new_file_name])

class Property(models.Model):

    street = models.CharField(max_length=255)

    city = models.CharField(max_length=255)
    
    state = models.CharField(max_length=255)
    
    zip_code = models.CharField(max_length=255)
    
    price = models.IntegerField()
    
    bedrooms = models.IntegerField()
    
    bathrooms = models.IntegerField()
    
    garage = models.IntegerField()
    
    square_feet = models.IntegerField()
    
    lot_size = models.DecimalField(decimal_places=2, max_digits=3)
    
    created_at = models.DateTimeField(auto_now_add=True)

    hero_image = models.ImageField(upload_to=upload_path)

    slide_img_1 = models.ImageField(upload_to=upload_path)

    slide_img_2 = models.ImageField(upload_to=upload_path)
    
    slide_img_3 = models.ImageField(upload_to=upload_path)
    
    slide_img_4 = models.ImageField(upload_to=upload_path)
    
    slide_img_5 = models.ImageField(upload_to=upload_path)
    
    slide_img_6 = models.ImageField(upload_to=upload_path)

    description = models.TextField(null=True, blank=True)

    class Meta:

        verbose_name_plural="Properties"
    
    def __str__(self):

        return self.street
