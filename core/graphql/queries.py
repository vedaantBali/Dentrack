import graphene
from .. import models
from . import types, resolvers

class Query(graphene.ObjectType):
    dentists = graphene.List(
        types.DentistType,
        id=graphene.Int(),
        resolver=resolvers.DentistResolver(),
    )