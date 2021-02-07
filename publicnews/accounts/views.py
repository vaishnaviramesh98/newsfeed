from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from .models import CustomUser,Feeds
from django.contrib import messages
from datetime import datetime

# Create your views here.
def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        # user = auth.authenticate(email=email,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')    

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dob=request.POST['dob']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if CustomUser.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif CustomUser.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:   
                user = CustomUser.objects.create_user(username=username, dob=dob,password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
                return redirect('login')

        else:
            messages.info(request,'password not matching..')    
            return redirect('register')
        return redirect('/')
        
    else:
        return render(request,'register.html')

        
    # else:
    #     return render(request,'register.html')



def logout(request):
    auth.logout(request)
    return redirect('/')       


def home(request):
    return render(request,'home.html')

def newsfeed(request):
    if request.method == 'POST':
        description = request.POST.get('feed')
        date = datetime.now()
        user = request.user
        feed = Feeds()
        feed.description = description
        feed.date = date
        feed.user = user
        feed.save()
        return redirect('view_feeds')
    return render(request,'newsfeed.html')

def view_feeds(request):
    feed1 = Feeds.objects.all().order_by('-date')
    usr = CustomUser.objects.all()
    return render(request, 'view_feed.html', {'feed': feed1, 'usr': usr})

def view_users(request):
    userlist1 = CustomUser.objects.all()
    return render(request,'view_users.html',{'userlist':userlist1})