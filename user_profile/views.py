from django.shortcuts import render, get_object_or_404
from .models import Profile
from .forms import *
from django.views.generic import UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy

# Create your views here.
class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'profiles/profile_detail.html'

    def get_object(self, queryset=None):
        obj = get_object_or_404(Profile, user=self.request.user)
        if obj.user != self.request.user:
            raise Http404
        return obj

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
    context={
        'user':user,
    }
    return render(request, 'user.html', context)
