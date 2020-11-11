from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Plant, PlantImage, User, Schedule
from .serializers import PlantSerializer


# Create your views here.
class PlantView(APIView):

    def get(self, request):
        plants = Plant.objects.all()
        serializer = PlantSerializer(plants, many=True)

        return Response(serializer.data)
