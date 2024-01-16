from .models import Hiretuber

def subject_renderer(request):
    return {'hiretuber': Hiretuber.objects.all(),}
    