from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            print("로그인 실패!")
            messages.add_message(request, messages.INFO, '회원 정보가 없습니다. 다시 입력해주세요')
            form=AuthenticationForm()
            return render(request, 'login.html',{'form':form})
    else:
        form=AuthenticationForm()
        return render(request, 'login.html',{'form':form})
    
def logout_view(request):
    logout(request)
    return redirect('home')

def signup_view(request):
    if request.method=='POST':
        # form=UserCreationForm(request.POST)
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
        return redirect('home')
    else:
        # form=UserCreationForm()
        form=RegisterForm()
        return render(request, 'signup.html',{'form':form})