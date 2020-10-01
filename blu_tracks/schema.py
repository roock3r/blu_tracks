import graphene

import main.schema

import main.users.schema

import graphql_jwt


class Query(main.users.schema.Query,main.schema.Query, graphene.ObjectType):
    pass


class Mutation(main.users.schema.Mutation,main.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

