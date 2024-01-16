from django.contrib import admin
from .models import Youtuber,YtResponseModel
from django.utils.html import format_html
# Register your models here.

class YTAdmin(admin.ModelAdmin):


    def myphoto(self, object):
        return format_html('<img src={} width = "40"/>'.format(object.photo.url))

    list_display = ('id','name','myphoto','subs_count', 'city', 'is_featured')
    list_display_links = ('id','name')
    list_editable = ('is_featured',)
    list_filter = ('city',)
    
admin.site.register(Youtuber, YTAdmin)

class YtResponseModelAdmin(admin.ModelAdmin):
    list_display = ('ytmsg',)

admin.site.register(YtResponseModel, YtResponseModelAdmin)