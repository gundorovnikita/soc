from django import forms
from .models import *
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['ava','city','status',]


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {
            'username',
        }

class CreateCity(forms.ModelForm):
    class Meta:
        model = City
        fields = ['text','slug',]

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =('text','slug','post','image',)
