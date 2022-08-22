from graphene_django import DjangoObjectType
from .. import models


class DentistType(DjangoObjectType):
    class Meta:
        model = models.Dentist
        fields = "__all__"

class InventoryType(DjangoObjectType):
    class Meta:
        model = models.Inventory
        fields = "__all__"

class ItemType(DjangoObjectType):
    class Meta:
        model = models.Item
        fields = ["id", "product", "count"]

class ProductType(DjangoObjectType):
    class Meta:
        model = models.Product
        exclude = ["item"]
