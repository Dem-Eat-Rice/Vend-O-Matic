from django.contrib import admin
from .models import Beverage, VendingMachine

admin.site.register(VendingMachine)
admin.site.register(Beverage)