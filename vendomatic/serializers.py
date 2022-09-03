from rest_framework import serializers
from .models import VendingMachine, Beverage

class VendingMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendingMachine
        fields = ['id', 'name', 'coin_count']

class BeverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beverage
        fields = ['id', 'type', 'cost', 'items_remaining', 'machine']