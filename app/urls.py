from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PlantView, PlantDetailView, ScheduleView, PlantImageView

urlpatterns = [
    path('plants/', PlantView.as_view()),
    path('plants/<int:pk>', PlantDetailView.as_view()),
    path('plants/<int:pk>/images/', PlantImageView.as_view()),
    path('schedules/', ScheduleView.as_view())
]

# urlpatterns = format_suffix_patterns(urlpatterns)
