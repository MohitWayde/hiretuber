
from django.contrib.messages.api import success
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404,redirect, render,HttpResponseRedirect
from .models import Youtuber, YtResponseModel
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from .forms import YoutuberUpdateForm
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView

# Create your views here.

def youtubers(request):
    youtubers = Youtuber.objects.order_by('-created_date')
    city_search = Youtuber.objects.values_list('city', flat=True).distinct()
    camera_type_search = Youtuber.objects.values_list('camera_type', flat=True).distinct()
    category_search = Youtuber.objects.values_list('category', flat=True).distinct()
    data ={
        'youtubers' : youtubers,
        'city_search':city_search,
        'camera_type_search':camera_type_search,
        'category_search':category_search,
    }
    return render(request,'youtubers/youtubers.html',data)

def youtubers_detail(request, id):
    tuber = get_object_or_404(Youtuber, pk=id)
    data = {
        'tuber':tuber
    }
    return render(request,'youtubers/youtuber_detail.html', data)

def search(request):
    youtubers = Youtuber.objects.order_by('-created_date')
    city_search = Youtuber.objects.values_list('city', flat=True).distinct()
    camera_type_search = Youtuber.objects.values_list('camera_type', flat=True).distinct()
    category_search = Youtuber.objects.values_list('category', flat=True).distinct()

    # for home page keyword
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            youtubers = youtubers.filter(description__icontains = keyword)

    # for youtubers page city wise search
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            youtubers = youtubers.filter(city__iexact = city)

    # for youtubers page camera_type wise search
    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            youtubers = youtubers.filter(camera_type__iexact = camera_type)

    # for youtubers page category wise search   
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            youtubers = youtubers.filter(category__iexact = category)

            
    data ={
        'youtubers' : youtubers,
        'city_search' : city_search,
        'camera_type_search' : camera_type_search,
        'category_search' : category_search,
    }
    return render(request,'youtubers/search.html',data)
    

# accounts

def selection_for_login(request):
    return render(request,"accounts/selection_for_login.html")

def selection_for_register(request):
    return render(request,"accounts/selection_for_register.html")
    
def register_youtuber(request):
    city_search = Youtuber.objects.values_list('city', flat=True).distinct()
    camera_type_search = Youtuber.objects.values_list('camera_type', flat=True).distinct()
    category_search = Youtuber.objects.values_list('category', flat=True).distinct()
    data ={

        'city_search':city_search,
        'camera_type_search':camera_type_search,
        'category_search':category_search,
    }
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        photo = request.FILES['photo']
        video_url = request.POST['video_url']
        description = request.POST['description']
        city = request.POST['city']
        age = request.POST['age']
        height = request.POST['height']
        crew = request.POST['crew']
        camera_type = request.POST['camera_type']
        subs_count = request.POST['subs_count']
        category = request.POST['category']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username already exists')
                return redirect('register_youtuber')
            else:
                if Youtuber.objects.filter(video_url=video_url).exists():
                    messages.warning(request, 'Video url already exists')
                    return redirect('register_youtuber')
                else:
                    youtuber = Youtuber(
                        name = name,
                        price = price,
                        photo = photo,
                        video_url = video_url,
                        description = description,
                        city = city,
                        age = age,
                        height = height,
                        crew = crew,
                        camera_type = camera_type,
                        subs_count = subs_count,
                        category = category,
                        # user=User.username,
                        
                    )
                    user = User.objects.create_user(
                        username = username,
                        password = password,
                    )
                    
                    youtuber.save()
                    user.save()
                    messages.success(request, 'Account created successfully')
                    return redirect('login_youtuber')
        else:
            messages.warning(request, 'password does not match')
            return redirect('register_youtuber')

    return render(request,'accounts/register_youtuber.html',data)

def login_youtuber(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username,password = password)

        if user is not None:
            auth.login(request,user)
            messages.success(request, 'Login successfully')
            return redirect('dashboard_youtuber')
        else:
            messages.warning(request, 'Invalid credentials')
            return redirect('login_youtuber')

    return render(request,'accounts/login_youtuber.html')

@login_required(login_url='login_youtuber')
def dashboard_youtuber(request):
    return render(request,"accounts/dashboard_youtuber.html")
    
class EditProfileView(UpdateView):
    template_name = 'accounts/edit_profile.html'
    model = Youtuber
    form_class = YoutuberUpdateForm
    context_object_name = 'context'
    query_pk_and_slug = True
    pk_url_kwarg = 'id'
    def get_success_url(self):
        messages.success(self.request, 'Profile update successfully')
        return '/'


def logout_youtuber(request):
    logout(request)
    return redirect('selection_for_login')



def ytresponseview(request):
    if request.method =='POST':
        ytmsg = request.POST['ytmsg']
        

        ytresponsemodel = YtResponseModel(
            ytmsg =  ytmsg,
            user = request.user
        )
        ytresponsemodel.save()
        messages.success(request, 'response sent successfully')
        return redirect('dashboard_youtuber')