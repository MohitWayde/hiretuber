from django.urls import path,include
from . import views

urlpatterns = [
    path('contactusform',views.contactusform,name='contactusform'),
    
]
