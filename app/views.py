from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Plant, PlantImage, User, Schedule
from .serializers import PlantSerializer, ScheduleSerializer


# Create your views here.
class PlantView(APIView):

    def get(self, request):
        plants = Plant.objects.all()
        serializer = PlantSerializer(plants, many=True)

        return Response(serializer.data)


class ScheduleView(APIView):

    def get(self, requrest):
        schedules = Schedule.objects.all()
        serializer = ScheduleSerializer(schedules, many=True)

        return Response(serializer.data)
