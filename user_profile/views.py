from django.shortcuts import render, get_object_or_404
from .models import Profile
from .forms import *
from django.views.generic import UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.
#class ProfileView(LoginRequiredMixin, DetailView):
#    model = Profile
#    context_object_name = 'profile'
#    template_name = 'profiles/profile_detail.html'
#
#    def get_object(self, queryset=None):
#        obj = get_object_or_404(Profile, user=self.request.user)
#        if obj.user != self.request.user:
#            raise Http404
#        return obj

def ProfileView(request):
    user = Profile.objects.get(user=request.user)
    posts = Post.objects.filter(profile=user)
    context={
        'user':user,
        'posts':posts,
    }
    return render(request, 'profiles/profile_detail.html', context)

def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(data=request.POST or None, instance = request.user)
        profile_form = ProfileForm(data=request.POST or None, instance=request.user.profile, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('view_profile')
    else:
        user_form = UserEditForm(instance = request.user)
        profile_form = ProfileForm(instance=request.user.profile)  # error
    context={
        'user_form':user_form,
        'profile_form':profile_form,
    }
    return render(request, 'profiles/profile_edit.html', context)

def create_city(request):
    if request.method == 'POST':
        city = CreateCity(data=request.POST or None)
        if city.is_valid():
            city.save()
            return redirect('edit_profile')
    else:
        city = CreateCity()
    context={
        'city':city,
    }
    return render(request, 'profiles/profile_edit_city.html', context)

def people(request):
    list = Profile.objects.all()
    context={
        'list':list,
    }
    return render(request, 'list.html', context)

def user_detail(request, slug):
    user = Profile.objects.get(slug=slug)
    if user.user == request.user:
        return HttpResponseRedirect(reverse('view_profile'))
    posts = Post.objects.filter(profile=user)
    context={
        'user':user,
        'posts':posts,
    }
    return render(request, 'user.html', context)

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    context={
        'post':post,
    }
    return render(request, 'post_detail.html', context)

def post_create(request):
    user = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        create = CreatePostForm(request.POST, request.FILES)
        if create.is_valid():
            post = create.save(commit=False)
            post.profile = user
            post.save()
            return redirect('view_profile')
    else:
        create = CreatePostForm()
    context= {
        'create': create,
    }
    return render(request, 'profiles/create_post.html', context)
