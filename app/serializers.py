from rest_framework import serializers
from .models import User, Plant, PlantImage, Schedule


class ScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedule
        fields = '__all__'


class PlantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plant
        fields = '__all__'

    schedules = ScheduleSerializer(
        many=True,
        read_only=True
    )
