from rest_framework import serializers
from . import models


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Branch
        fields = ('id', 'name')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = ('id', 'name', 'branch', 'category', 'product_code', 'created_on')
