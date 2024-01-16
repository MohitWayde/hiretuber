from django import forms
from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserModel
# Create your models here.
crew_choices = (
    ('solo','solo'),
    ('small','small'),
    ('large','large'),
)

camera_choices = (
    ('canon','canon'),
    ('nikon','nikon'),
    ('sony','sony'),
    ('red','red'),
    ('fuzi','fuzi'),
    ('panasonic','panasonic'),
    ('other','other'),
    
)

category_choices = (
    ('code','code'),
    ('product reviews','product reviews'),
    ('vlogs','vlogs'),
    ('comedy','comedy'),
    ('gaming','gaming'),
    ('film making','film making'),
    ('cooking','cooking'),
    ('inspiration','inspiration'),
    ('tricks and hacks','tricks and hacks'),
    ('education','education'),
    ('artist','artist'),
    ('news','news'),
    ('acting','acting'),
    ('unboxing','unboxing'),
    ('health and fitness','health and fitness'),
    ('philosophy','philosophy'),
    ('psychology','psychology'),
    ('spirituality','spirituality'),

)

class Youtuber(models.Model):
    user = models.CharField(null=True,max_length=255)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    photo = models.ImageField(null=True, blank=True,upload_to = 'media/ytubers/%Y/%m/')
    video_url = models.CharField(max_length=255)
    description = RichTextField()
    city = models.CharField(max_length=255)
    age = models.IntegerField(default="")
    height = models.IntegerField()
    crew = models.CharField(choices=crew_choices,max_length=255)
    camera_type = models.CharField(choices=camera_choices,max_length=255)
    subs_count = models.CharField(max_length=255)
    category = models.CharField(choices=category_choices,max_length=255)
    is_featured = models.BooleanField(default=False)
    created_date =models.DateTimeField(default=datetime.now(), blank=True)
   

    def __str__(self) -> str:
        return self.name


class YtResponseModel(models.Model):
    ytmsg = models.CharField(default="",max_length=50)
    user = models.CharField(default="",max_length=50)
    def __str__(self) -> str:
        return self.ytmsg


