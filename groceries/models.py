from django.db import models

PRODUCE = 'PRODUCE'
MEAT_SEAFOOD = 'MEAT/SEAFOOD'
DAIRY = 'DAIRY'
FROZEN_FOODS = 'FROZEN FOODS'
BREADS_PASTA = 'BREADS/PASTAS'
CANNED_GOODS = 'CANNED GOODS'
BREAKFAST = 'BREAKFAST'
SNACKS = 'SNACKS'
BAKING_CONDIMENTS = 'BAKING/CONDIMENTS'
BEVERAGES = 'BEVERAGES'
PAPER_PLASTIC = 'PAPER/PLASTIC'
CLEANING_PRODUCTS = 'CLEANING PRODUCTS'
TOILETRIES = 'TOILETRIES'
MISC = 'MISC'

GROCERY_ITEMS = (
    (PRODUCE, 'Produce'),
    (MEAT_SEAFOOD, 'Meat/Seafood'),
    (DAIRY, 'Dairy'),
    (FROZEN_FOODS, 'Frozen Foods'),
    (BREADS_PASTA, 'Breads/Pasta'),
    (CANNED_GOODS, 'Canned Goods'),
    (BREAKFAST, 'Breakfast'),
    (SNACKS, 'Snacks'),
    (BAKING_CONDIMENTS, 'Baking/Condiments'),
    (BEVERAGES, 'Beverages'),
    (PAPER_PLASTIC, 'Paper/Plastic'),
    (CLEANING_PRODUCTS, 'Cleaning Products'),
    (TOILETRIES, 'Toiletries'),
    (MISC, 'Miscellaneous')
)


class Item(models.Model):
    name = models.CharField(max_length=32)
    category = models.CharField(max_length=32, choices=GROCERY_ITEMS)
    quantity = models.IntegerField(null=True, blank=True)
    weight = models.DecimalField(null=True, blank=True, max_digits=4,
                                 decimal_places=2)

    def __str__(self):
        return self.name + ' - ' + self.category
