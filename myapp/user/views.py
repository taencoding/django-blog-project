from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
# from .models import User
from .forms import RegisterForm, LoginForm


# 회원가입
class Registration(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')
        
        form = RegisterForm()
        context = {
            'form': form,
            'title': 'User Registeration',
        }
        return render(request, 'user/register.html', context)
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user:login')
        

class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')
        
        form = LoginForm()
        context = {
            'form': form,
            'title': 'User Login',
        }
        return render(request, 'user/login.html', context)
    
    def post(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')
        
        form = LoginForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)

            if user:
                login(request, user)
                return redirect('blog:list')
            
        context = {
            'form': form
        }
        return render(request, 'user/login.html', context)
    


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('blog:list')