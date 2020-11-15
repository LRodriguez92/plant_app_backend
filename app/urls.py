from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url, include
from rest_framework import routers
# from .api import RegisterApi
from .views import PlantView, PlantDetailView, ScheduleView, PlantImageView, PlantImageDetailView, UserView

router = routers.DefaultRouter()
router.register(r'users', UserView)

urlpatterns = [
    path('plants/', PlantView.as_view()),
    path('plants/<int:pk>', PlantDetailView.as_view()),
    path('plants/<int:pk>/images/', PlantImageView.as_view()),
    path('plants/<int:pk>/images/<int:imagepk>',
         PlantImageDetailView.as_view()),
    path('plants/<int:pk>/schedule/', ScheduleView.as_view()),
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
    # path('register/', RegisterApi.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
