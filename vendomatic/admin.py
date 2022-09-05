from django.contrib import admin
from .models import Beverage, Inventory, VendingMachine

admin.site.register(VendingMachine)
admin.site.register(Inventory)
admin.site.register(Beverage)