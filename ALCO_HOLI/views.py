from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from .models import *
from .serializers import *



class getallinstrument(APIView):
    def get(self,result):
        result = list(instrument.objects.filter().values())
        return JsonResponse(result,status=status.HTTP_200_OK,safe=False)


class createinstrument(APIView):
    def post(self,request):
        inputdata = instrumentserializer(data = request.data)
        if inputdata.is_valid():
            instrument_name = inputdata.data['instrument_name']
            instrument_prize = inputdata.data['instrument_prize']
            instrument_quantity = inputdata.data['instrument_quantity']
            instrument_date = inputdata.data['instrument_date']

            instrument.objects.create(
                  instrument_name = instrument_name,
                  instrument_prize = instrument_prize,
                  instrument_quantity = instrument_quantity,
                  instrument_date = instrument_date
              )
            message = {'data': "instrument created successfully"}
            return JsonResponse (message,status=status.HTTP_200_OK)
        return JsonResponse (inputdata.errors,status=status.HTTP_200_OK)
