from unicodedata import name
from django.http import JsonResponse
from .models import Inventory, VendingMachine, Beverage
from .serializers import VendingMachineSerializer, BeverageSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Used for the '' url pathway
@api_view(['PUT', 'DELETE'])
def coin_function(request):
    vendingmachine = VendingMachine.objects.get(name='GoodYear Tire Lobby')
    if request.method == 'PUT':
        vendingmachine.add_coin(request.data['coin'])
        vendingmachine.save()
        return Response(status=status.HTTP_204_NO_CONTENT, headers={'X-Coins': request.data['coin']})
    elif request.method == 'DELETE':
        coins_to_dispense = vendingmachine.return_coin()
        vendingmachine.save()
        return Response(status=status.HTTP_204_NO_CONTENT, headers={'X-Coins': coins_to_dispense})


# Used for the 'inventory/' url pathway
@api_view(['GET'])
def inventory_count(request):
    remaining_soda = Beverage.objects.filter(name="SODA").count()
    remaining_water = Beverage.objects.filter(name="WATER").count()
    remaining_juice = Beverage.objects.filter(name="JUICE").count()
    remaining_beverages = [remaining_soda, remaining_water, remaining_juice]
    return Response(remaining_beverages, status=status.HTTP_200_OK)


# Used for inventory/<int:id>/' url pathway
@api_view(['GET', 'PUT'])
def type_count(request, id):
    beverage = Beverage.objects.get(id=id)
    inventory = Inventory.objects.get(name=beverage.inventory_name)
    vendingmachine = VendingMachine.objects.get(name=inventory.machine_name)

    print(inventory.name, inventory.machine_name, inventory.soda_count, inventory.water_count, inventory.juice_count)
    if request.method == 'GET':
        specific_beverage_count = Beverage.objects.filter(name=beverage).count()
        return Response(specific_beverage_count, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        
        return Response(status=status.HTTP_403_FORBIDDEN, headers={'X-Coins': vendingmachine.coin})

        
