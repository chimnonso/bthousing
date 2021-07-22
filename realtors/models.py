from django.db import models
from datetime import datetime

class Realtor(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/")
    description = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name