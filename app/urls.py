from django.urls import path
from .views import PlantView

urlpatterns = [
    path('plants/', PlantView.as_view())
]
