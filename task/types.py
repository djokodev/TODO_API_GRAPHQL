from task.models import Task
from graphene_django.types import DjangoObjectType
from graphene import relay

class TaskNode(DjangoObjectType):
    class Meta:
        model = Task
        filter_fields = ['title', 'completed']
        interfaces = (relay.Node, )