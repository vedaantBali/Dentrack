from graphene_django import DjangoObjectType
from .. import models
import graphene


class DentistType(DjangoObjectType):
    class Meta:
        model = models.Dentist
        fields = "__all__"


class InventoryType(DjangoObjectType):
    class Meta:
        model = models.Inventory
        fields = ["owner", "items"]


class ItemType(DjangoObjectType):
    # product = graphene.List(models.Product)
    class Meta:
        model = models.Item
        fields = ["id", "product", "count"]


class ProductType(DjangoObjectType):
    class Meta:
        model = models.Product
        fields = "__all__"
