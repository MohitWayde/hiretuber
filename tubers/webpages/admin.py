from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.db import models
from .models import Richaboutus, Slider,Team,Headandfoot
from django.utils.html import format_html

# Register your models here.

class SliderAdmin(ModelAdmin):
    def sliderimage(self, object):
        return format_html(f'<img src = {object.photo.url} width = "500" height = "100"/>')
    list_display = ('headline','button_text','sliderimage')

class TeamAdmin(admin.ModelAdmin):

    def myphoto(self, object):
        return format_html('<img src={} width = "40"/>'.format(object.photo.url))

    list_display = ('id','myphoto','first_name', 'role', 'created_date')
    list_display_links = ('id','first_name')
    search_fields = ('role','first_name')
    list_filter = ('role',)

admin.site.register(Slider, SliderAdmin)
admin.site.register(Team,TeamAdmin)
admin.site.register(Richaboutus)
admin.site.register(Headandfoot)