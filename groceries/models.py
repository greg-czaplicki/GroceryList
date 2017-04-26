from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=32, blank=False)
    category = models.CharField(max_length=32)
    quantity = models.IntegerField(default=1)
    weight = models.DecimalField(default=0,
                                 max_digits=4,
                                 decimal_places=2)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' - ' + self.category
