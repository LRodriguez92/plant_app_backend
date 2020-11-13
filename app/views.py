from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from .models import Plant, PlantImage, User, Schedule
from .serializers import PlantSerializer, ScheduleSerializer, PlantImageSerializer


# Create your views here.
class PlantView(APIView):
    # Only needs POST

    def get(self, request):
        plants = Plant.objects.all()
        serializer = PlantSerializer(plants, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = PlantSerializer(data=request.data)
        print(request.data)
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
    # Needs GET, PUT and DELETE

    # add pk as an argument to retrieve the pk in the parameter.
    def get(self, request, pk):
        try:
            plant = Plant.objects.get(id=pk)
        except:
            return Response({'message': 'The plant does not exist'})

        serializer = PlantSerializer(plant)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            plant = Plant.objects.get(id=pk)
        except:
            return Response({'message': 'The plant does not exist'})

        new_data = JSONParser().parse(request)
        serializer = PlantSerializer(plant, data=new_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            plant = Plant.objects.get(id=pk)
        except:
            return Response({'message': 'The plant does not exist'})

        plant.delete()
        return Response({'message': 'Plant was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


class PlantImageView(APIView):
    # add pk as an argument to retrieve the pk in the parameter.
    def get(self, request, pk):
        plants = PlantImage.objects.filter(plant=pk)
        serializer = PlantImageSerializer(plants, many=True)

        return Response(serializer.data)


class ScheduleView(APIView):
    # add pk as an argument to retrieve the pk in the parameter.
    def get(self, requrest, pk):
        schedule = Schedule.objects.get(plant=pk)
        serializer = ScheduleSerializer(schedule)

        return Response(serializer.data)
