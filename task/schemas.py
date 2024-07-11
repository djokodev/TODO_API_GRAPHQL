import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from task.models import Task
from task.types import TaskNode


class CreateTaskMutation(relay.ClientIDMutation):
    class Input:
        title = graphene.String(required=True)
        description = graphene.String()
        completed = graphene.Boolean()

    task = graphene.Field(TaskNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        task = Task(
            title = input.get('title'),
            description=input.get('description'),
            completed=input.get('completed', False)
        )
        task.save()
        return CreateTaskMutation(task=task)
    

class UpdateTaskMutation(relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)
        title = graphene.String()
        description = graphene.String()
        completed = graphene.Boolean()

    task = graphene.Field(TaskNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        task = relay.Node.get_node_from_global_id(info, input.get('id'))
        if task:
            task.title = input.get('title', task.title)
            task.description = input.get('description', task.description)
            task.completed = input.get('completed', task.completed)
            task.save()
        return UpdateTaskMutation(task=task)
    

class DeleteTaskMutation(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)

    task = graphene.Field(TaskNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        task = relay.Node.get_node_from_global_id(info, input.get('id'))
        if task:
            task.delete()
        return DeleteTaskMutation(task=task)
    

class Query(graphene.ObjectType):
    task = relay.Node.Field(TaskNode)
    all_tasks = DjangoFilterConnectionField(TaskNode)

class Mutation(graphene.ObjectType):
    create_task = CreateTaskMutation.Field()
    update_task = UpdateTaskMutation.Field()
    delete_task = DeleteTaskMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)