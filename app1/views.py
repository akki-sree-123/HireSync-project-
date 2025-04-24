# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required

def landingPage(request):
    return render(request,'landingPage.html')

@login_required(login_url='app1:login')
def homePage(request):
    data=request.user
    return render(request,'homePage.html',{'data':data})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('app1:home')  # Redirect to your home page
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after registration
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('app1:login')  # Redirect to your home page
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})



@login_required(login_url='app1:login')
def create_your_own_resume(request):
    return render(request,'create_your_own_resume.html')


def logout_view(request):
    logout(request)
    return redirect('app1:login')


def about_view(request):
    return render(request,'about.html')