from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Plant, PlantImage, User, Schedule

# Create your views here.


class PlantView(View):
    def get(self, request):
        plants = Plant.objects.all().values('id', 'plant_image', 'scientific_name', 'nickname', 'location', 'acquired',
                                            'special_instructions', 'user_id')  # only grab some attributes from our database, else we can't serialize it.
        # convert our artists to a list instead of QuerySet
        plants_list = list(plants)
        # safe=False is needed if the first parameter is not a dictionary.

        return JsonResponse(plants_list, safe=False)
