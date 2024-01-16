from .models import Youtuber, YtResponseModel
from django.shortcuts import get_object_or_404

def subject_renderer(request):
    return {
        'msgs':YtResponseModel.objects.all()
    }