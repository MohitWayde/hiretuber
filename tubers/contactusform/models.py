from datetime import datetime
from django.db import models
from django.db.models.base import Model

# Create your models here.
class Contactusform(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    company_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100, blank=True)
    message = models.TextField(blank=True)
    created_time = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.full_name
    
