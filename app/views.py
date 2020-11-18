from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny

from .permissions import IsLoggedInUserOrAdmin, IsAdminUser
from .models import Plant, PlantImage, User, UserProfile, Schedule
from .serializers import PlantSerializer, ScheduleSerializer, PlantImageSerializer, UserSerializer


# Create your views here.
class PlantView(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    # Needs GET and POST

    def get(self, request):
        user_id = request.user.id  # id of the current logged in user

        plants = Plant.objects.filter(user=user_id)
        serializer = PlantSerializer(plants, many=True)

        return Response(serializer.data)

    def post(self, request):
        # automatically add id of the user
        request.data["user"] = request.user.id
        serializer = PlantSerializer(data=request.data)

        if serializer.is_valid():
            # save to variable in order to access the id of the newly created plant
            saved_plant = serializer.save()

            plant_image = {
                'plant': saved_plant.id,
                'image': saved_plant.plant_image
            }
            image_serializer = PlantImageSerializer(
                data=plant_image)  # Save image to plant image table

            if image_serializer.is_valid():
                image_serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlantDetailView(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    # Needs GET, PUT and DELETE

    # add pk as an argument to retrieve the pk in the parameter.
    def get(self, request, pk):
        try:
            plant = Plant.objects.get(id=pk, user=request.user.id)
        except:
            return Response({'message': 'The plant does not exist'})

        serializer = PlantSerializer(plant)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            plant = Plant.objects.get(id=pk, user=request.user.id)
        except:
            return Response({'message': 'The plant does not exist'})

        new_data = JSONParser().parse(request)

        new_data["user"] = request.user.id  # add user id after parsing

        serializer = PlantSerializer(plant, data=new_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            plant = Plant.objects.get(id=pk, user=request.user.id)
        except:
            return Response({'message': 'The plant does not exist'})

        plant.delete()
        return Response({'message': 'Plant was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


class PlantImageView(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    # Needs GET and POST

    # add pk as an argument to retrieve the pk in the parameter.
    def get(self, request, pk):
        try:
            # verifies images get retrieved only from plants owned by users
            if Plant.objects.get(id=pk, user=request.user.id):
                images = PlantImage.objects.filter(plant=pk)
        except:
            return Response({'message': 'The images do not not exist'})

        serializer = PlantImageSerializer(images, many=True)

        return Response(serializer.data)

    def post(self, request, pk):
        request.data["plant"] = pk  # automatically add the plant id

        try:
            # verifies images get retrieved only from plants owned by users
            Plant.objects.get(id=pk, user=request.user.id)
        except:
            return Response({'message': 'The plant does not not exist'})

        serializer = PlantImageSerializer(
            data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlantImageDetailView(APIView):
    # Needs GET, PUT and DELETE

    def get(self, request, pk, imagepk):
        try:
            # verifies images get retrieved only from plants owned by users
            if Plant.objects.get(id=pk, user=request.user.id):
                image = PlantImage.objects.get(id=imagepk, plant=pk)
        except:
            return Response({'message': 'The image or plant does not exist'})

        serializer = PlantImageSerializer(image)
        return Response(serializer.data)

    def put(self, request, pk, imagepk):
        try:
            if Plant.objects.get(id=pk, user=request.user.id):
                image = PlantImage.objects.get(id=imagepk, plant=pk)
        except:
            return Response({'message': 'The image or plant does not exist'})

        new_data = JSONParser().parse(request)

        new_data["plant"] = pk  # add plant id after parsing

        serializer = PlantImageSerializer(image, data=new_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, imagepk):
        try:
            if Plant.objects.get(id=pk, user=request.user.id):
                image = PlantImage.objects.get(id=imagepk, plant=pk)
        except:
            return Response({'message': 'The image or plant does not exist'})

        image.delete()
        return Response({'message': 'Image was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


class ScheduleView(APIView):
    # Needs GET, POST, PUT and DELETE

    # add pk as an argument to retrieve the pk in the parameter.
    def get(self, requrest, pk):
        schedule = Schedule.objects.get(plant=pk)
        serializer = ScheduleSerializer(schedule)

        return Response(serializer.data)

    def post(self, request, pk):
        request.data["plant"] = pk  # automatically add the plant id

        serializer = ScheduleSerializer(
            data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            schedule = Schedule.objects.get(plant=pk)
        except:
            return Response({'message': 'The schedule does not exist'})

        new_data = JSONParser().parse(request)
        new_data["plant"] = pk  # automatically add plant id

        serializer = ScheduleSerializer(schedule, data=new_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            schedule = Schedule.objects.get(plant=pk)
        except:
            return Response({'message': 'The schedule does not exist'})

        schedule.delete()
        return Response({'message': 'Schedule was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'post':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def create(self, validated_data):
        # print('CREATING!!!!!!!!')
        # print(validated_data.data)
        profile_data = validated_data.data.pop('profile')
        # print("PROFILE DATA!!!!!")
        # print(profile_data)
        password = validated_data.data.pop('password')
        user = User(**validated_data.data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, photo=profile_data['photo'])
        return Response({'message': 'User created Successfully! Now perform Login to get your token'}, status=status.HTTP_201_CREATED)

    # def update(self, instance, validated_data):
    #     profile_data = validated_data.pop('profile')
    #     profile = instance.profile

    #     instance.email = validated_data.get('email', instance.email)
    #     instance.save()

    #     profile.photo = profile_data.get('photo', profile.photo)
    #     profile.save()

    #     return instance
