from django.contrib import admin
from .models import User, Plant, Schedule, Plant_Image


# Register your models here.
admin.site.register(User)
admin.site.register(Plant)
admin.site.register(Schedule)
admin.site.register(Plant_Image)
