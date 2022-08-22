from .. import models
from graphql import GraphQLError


class DentistResolver:
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
