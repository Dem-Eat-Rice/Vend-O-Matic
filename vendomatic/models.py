from django.db import models
# Models used to generate the database columns

class VendingMachine(models.Model):
    name = models.CharField(max_length=100)
    coin = models.PositiveIntegerField(default=0, null=False, blank=False)
    total_coin = models.PositiveIntegerField(default=0, null=True, blank=False)
    vended_items = models.PositiveIntegerField(default=0, null=False, blank=False)

    def __str__(self):
        return self.name

    def add_coin(self, coins):
        self.coin += coins
        self.coin
        return self.coin

    def return_coin(self):
        coins_returned = self.coin
        self.coin = 0
        return coins_returned

    def item_vended(self):
        if self.coin >= 2:
            self.coin -= 2
            self.total_coin += 2
        return self.coin

    def vended_items_count(self):
        self.vended_items += 1
        return self.vended_items


class Inventory(models.Model):
    name = models.CharField(max_length=100)
    machine_name = models.OneToOneField(VendingMachine, on_delete=models.CASCADE, null=True, blank=True)
    soda_count = models.PositiveIntegerField(default=5,  null=False, blank=False)
    water_count = models.PositiveIntegerField(default=5, null=False, blank=False)
    juice_count = models.PositiveIntegerField(default=5, null=False, blank=False)
    
    def __str__(self):
        return self.name
# Checks the name being passed in to update the appropriate beverage counts above
    def item_vended(self, name):
        if (name == 'SODA') and (self.soda_count > 0):
                self.soda_count -= 1
                return 1
        elif (name == 'WATER') and (self.water_count > 0):
                self.water_count -= 1
                return 1
        elif (name == 'JUICE') and (self.juice_count > 0):
                self.juice_count -= 1
                return 1
        else:
            return False

    def get_item_count(self, name):
        if name == 'SODA':
            return self.soda_count
        elif name == 'WATER':
            return self.water_count
        elif name == 'JUICE':
            return self.juice_count
        
    def get_inventory_count(self):
        total_list = [self.soda_count, self.water_count, self.juice_count]
        return total_list
    



class Beverage(models.Model):
    
    typeofbeverage = (
        ('SODA', 'SODA'),
        ('WATER', 'WATER'),
        ('JUICE', 'JUICE'),
    )
# name field will be limited to the choices in typesofbeverage
    name = models.CharField(max_length=5, choices=typeofbeverage, null=True, blank=True)
    cost = models.IntegerField(default=2)
    inventory_name = models.ForeignKey('Inventory', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.name





