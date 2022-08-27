import graphene
from . import types, resolvers


class Query(graphene.ObjectType):
    dentists = graphene.List(
        types.DentistType,
        id=graphene.Int(),
        resolver=resolvers.DentistListResolver(),
    )

    inventory_by_dentist = graphene.List(
        types.InventoryType,
        id=graphene.Int(),
        resolver=resolvers.InventoryResolver(),
    )
