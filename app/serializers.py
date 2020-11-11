from rest_framework import serializers
from .models import User, Plant, PlantImage, Schedule


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'
