from rest_framework import serializers
from .models import User, Plant, PlantImage, Schedule


class PlantImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlantImage
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedule
        fields = '__all__'


class PlantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plant
        fields = '__all__'

    schedule = ScheduleSerializer(
        many=False,
        read_only=True
    )

    images = PlantImageSerializer(
        many=True,
        read_only=True
    )
