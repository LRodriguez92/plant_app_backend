from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from .views import PlantView, PlantDetailView, ScheduleView, PlantImageView, PlantImageDetailView, UserView, UserProfileView, TrefleView

router = routers.DefaultRouter()
router.register(r'users', UserView)  # Use this route to create users

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
    path('users/<int:pk>/profile/', UserProfileView.as_view()),
    path('plants/', PlantView.as_view()),
    path('plants/<int:pk>/', PlantDetailView.as_view()),
    path('plants/<int:pk>/images/', PlantImageView.as_view()),
    path('plants/<int:pk>/images/<int:imagepk>/',
         PlantImageDetailView.as_view()),
    path('plants/<int:pk>/schedule/', ScheduleView.as_view()),
    path('trefle/plants/<str:name>', TrefleView.as_view())
]
