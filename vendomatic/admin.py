from django.contrib import admin
from .models import VendingMachine, Drink

admin.site.register(VendingMachine)
admin.site.register(Drink)