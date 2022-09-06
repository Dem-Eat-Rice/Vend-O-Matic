from rest_framework import serializers
from .models import VendingMachine, Inventory, Beverage

# These serializers would be utilized if I needed to send back models in JSON

class VendingMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendingMachine
        fields = ['id', 'name', 'coin', 'total_coin', 'vended_items']

class BeverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beverage
        fields = ['id', 'name', 'cost', 'inventory_name']

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['id', 'name', 'machine_name', 'soda_count', 'water_count', 'juice_count']
