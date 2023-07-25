from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
# from .models import User
from .forms import RegisterForm, LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
# from .models import Profile


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
    

class PasswordChange(LoginRequiredMixin, View):
    def get(self, request):
        form = PasswordChangeForm(request.user)
        context = {
            'form': form,
        }
        return render(request, 'user/pw_change.html', context)
    
    def post(self, request):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            # logout(request)
            return redirect('user:login')

        context = {
            'form': form,
        }
        return render(request, 'user/pw_change.html', context)

# class Profile(LoginRequiredMixin, View):
#     def get(self, reuset, pk):
#         user = User.objects.get(pk=pk)
#         form = UserF
#         return
    
#     def post(self, request, pk):

#         return