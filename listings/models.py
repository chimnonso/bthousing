from django.db import models
from django.db.models.deletion import DO_NOTHING
from realtors.models import Realtor

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    price = models.IntegerField()
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    description = models.TextField(blank=True)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(decimal_places=1, max_digits=5)
    photo_main = models.ImageField(upload_to="photos/%Y/%m/%d/")
    photo_1 = models.ImageField(upload_to="photo/%Y/%m/%d/")
    photo_2 = models.ImageField(upload_to="photo/%Y/%m/%d/")
    photo_3 = models.ImageField(upload_to="photo/%Y/%m/%d/")
    photo_4 = models.ImageField(upload_to="photo/%Y/%m/%d/")
    photo_5 = models.ImageField(upload_to="photo/%Y/%m/%d/")
    photo_6 = models.ImageField(upload_to="photo/%Y/%m/%d/")
