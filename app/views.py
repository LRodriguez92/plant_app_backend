from django.shortcuts import render
from django.http import JsonResponse
from django.views import View


# Create your views here.
class MyAPIView(View):
    def get(self, request):
        data = {
            'name': request.user.username,
            'url': 'https://www.pyscoop.com/',
            'skills': ['Python', 'Django'],
        }

        return JsonResponse(data)
