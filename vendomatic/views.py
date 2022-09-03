from unicodedata import name
from django.http import JsonResponse
from .models import VendingMachine, Beverage
from .serializers import VendingMachineSerializer, BeverageSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['PUT', 'DELETE'])
def coin_function(request):
    if request.method == 'PUT':
        print(request.body)
    elif request.method == 'DELETE':
        pass

@api_view(['GET'])
def inventory_count(request):
    remaining_soda = Beverage.objects.filter(type='Soda').count()
    remaining_water = Beverage.objects.filter(type='Water').count()
    remaining_juice = Beverage.objects.filter(type='Juice').count()
    remaining_beverages = [remaining_soda, remaining_water, remaining_juice]
    return Response(remaining_beverages, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT'])
def type_count(request, id):
    if request.method == 'GET':
        beverage = Beverage.objects.get(id=id)
        specific_beverage = Beverage.objects.filter(type=beverage)
        return Response(specific_beverage, status=status.HTTP_200_OK)
    elif request.method == 'PUT':

        return Response({'quantity': 'COME BACK TO THIS'}, status=status.HTTP_200_OK)
