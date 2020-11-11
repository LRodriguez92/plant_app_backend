from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PlantView, ScheduleView, PlantImageView

urlpatterns = [
    path('plants/', PlantView.as_view()),
    path('images/', PlantImageView.as_view()),
    path('schedules/', ScheduleView.as_view())
]

# urlpatterns = format_suffix_patterns(urlpatterns)
