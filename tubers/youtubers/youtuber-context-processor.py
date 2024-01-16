from .models import Youtuber
from django.shortcuts import get_object_or_404

def subject_renderer(request):
    return {
        # 'allyoutubers': get_object_or_404(Youtuber, pk=id)
        'mytuber': Youtuber.objects.all
    }