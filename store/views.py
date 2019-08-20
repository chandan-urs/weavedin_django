from rest_framework import viewsets
from . import serializer
from . import models


class BranchViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.BranchSerializer
    queryset = models.Branch.objects.all()


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.ItemSerializer
    queryset = models.Item.objects.all()
