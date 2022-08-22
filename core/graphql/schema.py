import graphene
from core.graphql.mutations import Mutation
from core.graphql.queries import Query

schema = graphene.Schema(query=Query, mutation=Mutation)
