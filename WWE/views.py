from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from .models import *
from .serializers import *


class getallcharacter(APIView):
    def get(self,request):
        result = list(character.objects.filter().values())
        return JsonResponse(result,status=status.HTTP_200_OK,safe=False)


class createcharacter(APIView):
    def post(self,request):
        inputdata = characterserializer(data = request.data)
        if inputdata.is_valid():
            character_name = inputdata.data['character_name']
            character_price = inputdata.data['character_price']
            character_quantity = inputdata.data['character_quantity']
            character_date = inputdata.data['character_date']

            character.objects.create(
                  character_name = character_name,
                  character_price = character_price,
                  character_quantity = character_quantity,
                  character_date = character_date
              )
            message = {'data': "character created successfully"}
            return JsonResponse (message,status=status.HTTP_200_OK)
        return JsonResponse (inputdata.errors,status=status.HTTP_200_OK)