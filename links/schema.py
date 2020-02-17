import graphene
from graphene_django import DjangoObjectType

from .models import Link


class LinkType(DjangoObjectType):
    class Meta:
        model = Link

class Query(graphene.ObjectType):
    links = graphene.List(LinkType)

    def resolve_links(self, info, **kwargs):
        return Link.objects.all()

#1
class CreateLink(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()

    #2  Deines Data that can be sent to the Server, Here url and description can be sent
    class Arguments:
        url = graphene.String()
        description = graphene.String()

    #3 The Mutation Method
    def mutate(self, info, url, description):
        link = Link(url=url, description=description)
        link.save()

        new_link = CreateLink(id= link.id, url = link.url, description = link.description)

        return new_link

#4
class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()
