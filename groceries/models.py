from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=32)
    quantity = models.IntegerField()
    weight = models.IntegerField()


class Produce(Item):
    pass


class Meat_Seafood(Item):
    pass


class Dairy(Item):
    pass


class Frozen_Food(Item):
    pass


class Breads_Pasta(Item):
    pass


class Canned_Goods(Item):
    pass


class Snacks(Item):
    pass


class Baking_Condiments(Item):
    pass


class Paper_Plastic(Item):
    pass


class Cleaning_Products(Item):
    pass


class Toiletries(Item):
    pass


class Misc(Item):
    pass
