from django.contrib import admin
from .models import Hiretuber

# Register your models here.
# class AccountsAdmin(admin.ModelAdmin):
#     list_display = ('id','E-mail address','User','Primary','Verified')

# admin.site.register(AccountsAdmin)



# Register your models here.

class HiretuberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email','tuber_name')
    list_display_links = ('first_name', 'email')

admin.site.register(Hiretuber,HiretuberAdmin)