from django.db import models
from django.contrib.postgres.fields import ArrayField


class Branch(models.Model):
    """Model for branch"""
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    """Model for items in a branch"""
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    product_code = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Variant(models.Model):
    """Model for variants in a branch"""
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    selling_price = models.FloatField(default=0.0)
    cost_price = models.FloatField(default=0.0)
    properties = ArrayField(
        models.CharField(max_length=255), null=True, blank=True
    )
    quantity = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item.name + ":" + self.name

