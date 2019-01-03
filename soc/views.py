from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from user_profile.models import Profile


def user_login(request):
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('login_url'))
                else:
                    return HttpResponseRedirect('user is not active')
            else:
                return HttpResponse('user is not')
    else:
        form = UserLogin()
    context = {
        'form':form,
    }
    return render(request, 'startpage.html', context)

def user_logout(request):
    logout(request)
    return redirect('login_url')

def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            #Profile.objects.create(user=new_user)
            logout(request)
            return redirect('login_url')
    else:
        form = UserRegistration()
    context = {
        'form':form,
    }
    return render(request,'register.html', context)
