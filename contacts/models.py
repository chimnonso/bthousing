from django.db import models
from datetime import datetime

class Contact(models.Model):
    user_id = models.IntegerField()
    listing_id = models.IntegerField()
    message = models.TextField()
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    listing = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
