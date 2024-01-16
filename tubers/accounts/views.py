from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from .models import Hiretuber


# Create your views here.
def hiretuber(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        tuber_id = request.POST['tuber_id']
        tuber_name = request.POST['tuber_name']
        city = request.POST['city']
        phone = request.POST['phone']
        state = request.POST['state']
        message = request.POST['message']
        user_id = request.POST['user_id']
        email = request.POST['email']
       


        # If i have to do sanitization of data

        hire = Hiretuber(first_name = first_name,
        last_name = last_name,
        tuber_id = tuber_id,
        tuber_name = tuber_name,
        city = city,
        phone = phone,
        state = state,
        message = message,
        user_id = user_id,
        email = email,
        
        )

        hire.save()
        messages.success(request, 'Thanks for reach out!')
        return redirect('youtubers')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username,password = password)

        if user is not None:
            auth.login(request,user)
            messages.success(request, 'Login successfully')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Invalid credentials')
            return redirect('login')

    

    return render(request,'accounts/login.html')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.warning(request, 'Email address already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        first_name = firstname,
                        last_name = lastname,
                        username = username,
                        email = email,
                        password = password,
                    )

                    user.save()
                    messages.success(request, 'Account created successfully')
                    return redirect('login')
        else:
            messages.warning(request, 'password does not match')
            return redirect('register')

    return render(request,'accounts/register.html')

    
def logout_user(request):
    logout(request)
    return redirect('selection_for_login')

@login_required(login_url='login')
def dashboard(request):
    hiredata = Hiretuber.objects.all()
    # hiredata = Hiretuber.filter(User.first_name==Hiretuber.first_name)#Hiretuber.first_name == User.first_name
    data = {
        'hiredata':hiredata,
    }
    return render(request,'accounts/dashboard.html',data)


