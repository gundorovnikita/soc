from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ProfileView, name='view_profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('edit_profile/city', create_city, name='create_city'),
    path('create', post_create, name='post_create_url'),
    path('list', people, name='people_url'),
    path('m/<str:slug>', user_detail, name='user_detail_url'),
    path('p/<str:slug>', post_detail, name='post_detail_url'),
    #path('usr/', include('user_profile.urls'), name='usr'),
]
