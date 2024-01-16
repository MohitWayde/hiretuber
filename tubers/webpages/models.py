from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Team(models.Model):
    first_name = models.CharField(max_length=255)    
    last_name = models.CharField(max_length=255)    
    role = models.CharField(max_length=255)    
    fb_link = models.CharField(max_length=255)    
    insta_link = models.CharField(max_length=255)    
    photo = models.ImageField(upload_to = "media/team/%Y/%m/%d/")
    created_date = models.DateTimeField(auto_now_add=True)
    yt_link = models.CharField(max_length=255, default="")    

    def __str__(self) ->str:
        return self.first_name
        
class Slider(models.Model):
    """
    Used for slider images used for websites
    """
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    photo = models.ImageField(upload_to = 'media/slider/%Y/')
    created_date = models.DateTimeField(auto_now_add=True)
    buttonlink = models.CharField(max_length=255, default="")

    def __str__(self) -> str:
        return self.headline

class Richaboutus(models.Model):
    richeditor  = RichTextField()

class Headandfoot(models.Model):
    mailbyuser = models.CharField(max_length=255) 
    numberbyuser = models.CharField(max_length=255)
    instalink = models.CharField(max_length=255)
    facebooklink = models.CharField(max_length=255)
    twitterlink = models.CharField(max_length=255)
    youtubelink = models.CharField(max_length=255)