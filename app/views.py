from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Plant, PlantImage, User, Schedule
from .serializers import PlantSerializer, ScheduleSerializer, PlantImageSerializer


# Create your views here.
class PlantView(APIView):
    def get(self, request):
        plants = Plant.objects.all()
        serializer = PlantSerializer(plants, many=True)

        return Response(serializer.data)


class PlantDetailView(APIView):
    # add pk as an argument to retrieve the pk in the parameter.
    def get(self, request, pk):
        plant = Plant.objects.get(id=pk)
        serializer = PlantSerializer(plant)

        return Response(serializer.data)


class PlantImageView(APIView):
    # add pk as an argument to retrieve the pk in the parameter.
    def get(self, request, pk):
        plants = PlantImage.objects.filter(plant=pk)
        serializer = PlantImageSerializer(plants, many=True)

        return Response(serializer.data)


class ScheduleView(APIView):
    # add pk as an argument to retrieve the pk in the parameter.
    def get(self, requrest, pk):
        schedules = Schedule.objects.get(plant=pk)
        serializer = ScheduleSerializer(schedules)

        return Response(serializer.data)
