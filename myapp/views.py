from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Product

def index(request):
    return render(request, 'index.html')

def farmer(request):
    return render(request, 'farmer.html')


def add(request):
    
    return render(request, 'add.html',{'username': request.user.username})


def remove(request):
    return render(request,'remove.html',{'username': request.user.username})


def update(request):
   return render(request, 'update.html',{'username': request.user.username})


def view(request):
    return render(request, 'view.html', {'username': request.user.username})


def customer(request):
    return render(request, 'customer.html')

def register(request):
    if request.method == "POST":
        user = request.POST['username']
        email = request.POST['email']
        p1 = request.POST['password1']
        p2 = request.POST['password2']
        if p1 == p2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('register')
            elif User.objects.filter(username=user).exists():
                messages.info(request, 'Username not available')
                return redirect('register')
            else:
                user = User.objects.create_user(username=user, email=email, password=p1)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    return render(request, 'register.html')


def cust_register(request):
    if request.method == "POST":
        user = request.POST['username']
        email = request.POST['email']
        p1 = request.POST['password1']
        p2 = request.POST['password2']
        if p1 == p2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('cust_register')
            elif User.objects.filter(username=user).exists():
                messages.info(request, 'Username not available')
                return redirect('cust_register')
            else:
                user = User.objects.create_user(username=user, email=email, password=p1)
                user.save()
                return redirect('cust_login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('cust_register')
    return render(request, 'cust_register.html')

def login(request):
    if request.method == "POST":
        user = request.POST['username']
        pas = request.POST['password']
        user = auth.authenticate(username=user, password=pas)
        
        if user is not None:
            auth.login(request, user)
            return redirect('farmer')
        else:
            messages.info(request, 'INVALID DETAILS')
            return redirect('login')
    else:
        return render(request, 'login.html')


def cust_login(request):
    if request.method == "POST":
        user = request.POST['username']
        pas = request.POST['password']
        user = auth.authenticate(username=user, password=pas)
        
        if user is not None:
            auth.login(request, user)
            return redirect('customer')
        else:
            messages.info(request, 'Invalid details')
            return redirect('cust_login')
    else:
        return render(request, 'cust_login.html')