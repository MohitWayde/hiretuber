from django.db import models

from datetime import datetime

# Create your models here.


# Create your models here.
class Hiretuber(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    tuber_id = models.IntegerField()
    tuber_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    state = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    created_date = models.DateTimeField(default=datetime.now())
    email = models.EmailField(max_length=100)
    

    def __str__(self):
        return self.email