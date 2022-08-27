from .. import models
from graphql import GraphQLError


class DentistListResolver:
    def __call__(self, name, info, **kwargs):
        user = info.context.user
        id = kwargs.get("id")
        try:
            query = models.Dentist.objects.all()
            if id:
                return query.filter(id=id)
            return query
        except Exception as e:
            print(e)
        return None


class InventoryResolver:
    def __call__(self, name, info, **kwargs):
        this_user = info.context.user
        dentist = models.Dentist.objects.get(name="dentist1")
        query = models.Inventory.objects.get(owner=dentist)
        return query