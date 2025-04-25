from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def register(request):
    if request.method == 'POST':
        userName = request.POST['userName']
        password = request.POST['password']
        if User.objects.filter(userName=userName).exists():
            messages.error(request, 'ID already exists, please change it')
            return redirect('register')
        else:
            user = User(userName=userName, password=password)
            user.save()
            messages.success(request, 'Registered successfully')
            return redirect('login')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        userName = request.POST['userName']
        password = request.POST['password']
        user = User.objects.filter(userName=userName, password=password).first()
        if user is not None:
            messages.success(request, 'Login successfully')
            return redirect('home')
        else:
            messages.error(request, 'ID or password error')
            return redirect('login')
    return render(request, 'login.html')