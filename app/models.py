from django.db import models
# import the following to create a user
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

# Create your models here.

# Extend from Django's user


class User(AbstractUser):
    username = models.CharField(blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)

# Add fields for the user by creating OneToOne relationship


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(upload_to='uploads', blank=True)


class Plant(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='plants')
    plant_image = models.TextField(null=True)
    scientific_name = models.CharField(max_length=100, null=True)
    nickname = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    acquired = models.DateField(null=True)
    special_instructions = models.TextField(null=True)

    def __str__(self):
        return self.nickname


class Schedule(models.Model):
    plant = models.OneToOneField(
        Plant, on_delete=models.CASCADE, primary_key=True, related_name='schedule')
    water_date = models.DateField(null=True)
    water_time = models.TimeField(null=True)
    water_repeat = models.IntegerField(null=True)
    water_notification = models.BooleanField(default=True)
    fertilize_date = models.DateField(null=True)
    fertilize_time = models.TimeField(null=True)
    fertilize_repeat = models.IntegerField(null=True)
    fertilize_notification = models.BooleanField(default=True)
    rotate_date = models.DateField(null=True)
    rotate_time = models.TimeField(null=True)
    rotate_repeat = models.IntegerField(null=True)
    rotate_notification = models.BooleanField(default=True)
    repot_date = models.DateField(null=True)
    repot_time = models.TimeField(null=True)
    repot_repeat = models.IntegerField(null=True)
    repot_notification = models.BooleanField(default=True)
    mist_date = models.DateField(null=True)
    mist_time = models.TimeField(null=True)
    mist_repeat = models.IntegerField(null=True)
    mist_notification = models.BooleanField(default=True)


class PlantImage(models.Model):
    plant = models.ForeignKey(
        Plant, on_delete=models.CASCADE, related_name='images')
    image = models.TextField()
