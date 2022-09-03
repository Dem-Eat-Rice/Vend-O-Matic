from unicodedata import name
from django.http import JsonResponse
from .models import VendingMachine, Beverage
from .serializers import VendingMachineSerializer, BeverageSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def inventory_count(request):
    soda = Beverage.objects.filter(type='Soda')
    water = Beverage.objects.filter(type='Water')
    juice = Beverage.objects.filter(type='Juice')
    remaining_soda = len(soda)
    remaining_water = len(water)
    remaining_juice = len(juice)
    remaining_beverages = [remaining_soda, remaining_water, remaining_juice ]

    return JsonResponse(remaining_beverages, safe=False)
