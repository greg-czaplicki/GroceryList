from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=32)
    category = models.CharField(max_length=32)
    quantity = models.IntegerField(null=True, blank=True)
    weight = models.DecimalField(null=True, blank=True, max_digits=4,
                                 decimal_places=2)

    def __str__(self):
        return self.name + ' - ' + self.category
