from .models import Youtuber
from django.forms import ModelForm

# Create your models here.

class YoutuberUpdateForm(ModelForm):
    class Meta:
        model = Youtuber
        fields = [
            'name','price','photo','video_url',
            'description','city','age','height',
            'crew','camera_type','subs_count',
            'category'
        ]
