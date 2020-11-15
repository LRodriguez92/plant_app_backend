from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from .models import Plant, PlantImage, Schedule, User, UserProfile


class PlantImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlantImage
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedule
        fields = '__all__'


class PlantSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

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


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('url', 'email', 'first_name',
                  'last_name', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.photo = profile_data.get('photo', profile.photo)
        profile.save()

        return instance
