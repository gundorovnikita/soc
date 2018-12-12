from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

# Create your models here.
class City(models.Model):
    text = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    def __str__(self):
        return self.slug

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ava = models.ImageField()
    slug = models.SlugField(max_length=100, unique=True, null=True)
    images = models.ManyToManyField('Images',related_name='images',blank=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super(Profile, self).save(*args, **kwargs)
    def __str__(self):
        return self.slug
    def get_absolute_url(self):
        return reverse('user_detail_url', kwargs={'slug': self.slug})
    def get_avatar_url(self):
        if self.ava:
            return '/media/{}'.format(self.ava)
        else:
            return '/static/img/default.png'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Создание профиля пользователя при регистрации"""
    if created:
        Profile.objects.create(user=instance, id=instance.id)

class Images(models.Model):
    image = models.ImageField()
    slug = models.SlugField(max_length=100, unique=True)
    def __str__(self):
        return self.slug
