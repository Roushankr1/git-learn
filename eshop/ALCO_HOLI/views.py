from rest_framework.views import ALCO_HOLIView
from django.http import JsonResponse
from rest_framework import status
from .models import *


class getallinstrument(ALCO_HOLIView):
    def get(self,result):
        result = list(instrument.objects.filter().values())
        return JsonResponse(result,status=status.HTTP_200_OK,safe=False)