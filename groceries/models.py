from django.db import models


class Produce(models.Model):
    name = models.CharField(max_length=32)
    quantity = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Produce'
        verbose_name_plural = 'Produce'

    def get_cname(self):
        class_name = 'Produce'
        return class_name

    def __str__(self):
        return self.name


class Meat_Seafood(models.Model):
    name = models.CharField(max_length=32)
    quantity = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Meat/Seafood'
        verbose_name_plural = 'Meat/Seafood'

    def get_cname(self):
        class_name = 'Meat/Seafood'
        return class_name

    def __str__(self):
        return self.name


class Dairy(models.Model):
    name = models.CharField(max_length=32)
    quantity = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Dairy'
        verbose_name_plural = 'Dairy'

    def get_cname(self):
        class_name = 'Dairy'
        return class_name

    def __str__(self):
        return self.name


class Frozen_Food(models.Model):
    name = models.CharField(max_length=32)
    quantity = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Frozen Food'
        verbose_name_plural = 'Frozen Food'

    def get_cname(self):
        class_name = 'Frozen Food'
        return class_name

    def __str__(self):
        return self.name


class Breads_Pasta(models.Model):
    name = models.CharField(max_length=32)
    quantity = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Breads/Pasta'
        verbose_name_plural = 'Breads/Pasta'

    def get_cname(self):
        class_name = 'Breads/Pasta'
        return class_name

    def __str__(self):
        return self.name


class Canned_Goods(models.Model):
    name = models.CharField(max_length=32)
    quantity = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Canned Goods'
        verbose_name_plural = 'Canned Goods'

    def get_cname(self):
        class_name = 'Canned Goods'
        return class_name

    def __str__(self):
        return self.name


class Snacks(models.Model):
    name = models.CharField(max_length=32)
    quantity = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Snacks'
        verbose_name_plural = 'Snacks'

    def get_cname(self):
        class_name = 'Snacks'
        return class_name

    def __str__(self):
        return self.name


class Baking_Condiments(models.Model):
    name = models.CharField(max_length=32)
    quantity = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Baking Condiments'
        verbose_name_plural = 'Baking Condiments'

    def get_cname(self):
        class_name = 'Baking Condiments'
        return class_name

    def __str__(self):
        return self.name


class Paper_Plastic(models.Model):
    name = models.CharField(max_length=32)
    quantity = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Paper/Plastic'
        verbose_name_plural = 'Paper/Plastic'

    def get_cname(self):
        class_name = 'Paper/Plastic'
        return class_name

    def __str__(self):
        return self.name


class Cleaning_Products(models.Model):
    name = models.CharField(max_length=32)
    quantity = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Cleaning Products'
        verbose_name_plural = 'Cleaning Products'

    def get_cname(self):
        class_name = 'Cleaning Products'
        return class_name

    def __str__(self):
        return self.name


class Toiletries(models.Model):
    name = models.CharField(max_length=32)
    quantity = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Toiletries'
        verbose_name_plural = 'Toiletries'

    def get_cname(self):
        class_name = 'Toiletries'
        return class_name

    def __str__(self):
        return self.name


class Misc(models.Model):
    name = models.CharField(max_length=32)
    quantity = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Misc'
        verbose_name_plural = 'Misc'

    def get_cname(self):
        class_name = 'Misc.'
        return class_name

    def __str__(self):
        return self.name
