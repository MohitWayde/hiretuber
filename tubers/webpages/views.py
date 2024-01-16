from django.shortcuts import get_object_or_404, render
from .models import Richaboutus, Slider,Team
from youtubers.models import Youtuber
# Create your views here.

def home(request):
    sliders = Slider.objects.all()
    teams = Team.objects.all()
    featured_youtubers = Youtuber.objects.order_by('-created_date').filter(is_featured = True)
    # need to be check below code
    all_youtubers = Youtuber.objects.all()
    
    # For non featured youtubers only (below code)
    # all_youtubers = Youtuber.objects.filter(is_featured = False)

    data = {
        'sliders':sliders,
        'teams' : teams,
        'featured_youtubers': featured_youtubers,
        'all_youtubers' : all_youtubers
    }
    return render(request, 'webpages/home.html',data)

def about(request):
    richaboutus = get_object_or_404(Richaboutus)
    teams = Team.objects.all()
    data = {
        'teams':teams,
        'richaboutus':richaboutus,
    }
    return render(request, 'webpages/about.html',data)

def services(request):
    return render(request, 'webpages/services.html')

def contact(request):
    return render(request, 'webpages/contact.html')


