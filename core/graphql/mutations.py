import graphene
from .. import models


class ModifyDentistName(graphene.Mutation):
    ok = graphene.Boolean()
    error = graphene.String()

    class Arguments:
        owner_id = graphene.Int()
        new_name = graphene.String()

    def mutate(name, info, owner_id, new_name):
        user = info.context.user
        try:
            dentist = models.Dentist.objects.get(id=owner_id)
            if user.id != owner_id:
                return {"ok": False, "error": "You are not allowed to edit this user"}
            dentist.name = new_name
            dentist.save()
            return {"ok": True, "error": None}
        except models.Dentist.DoesNotExist:
            return {"ok": False, "error": "No dentist found for this user"}


class Mutation(graphene.ObjectType):
    modify_dentist_name = ModifyDentistName.Field()
