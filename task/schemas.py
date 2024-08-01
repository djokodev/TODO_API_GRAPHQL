import graphene
from graphene import relay
from .models import Task
from .types import TaskNode


class CreateTaskInput(graphene.InputObjectType):
    title = graphene.String(required=True)
    description = graphene.String()
    completed = graphene.Boolean()


class CreateTaskMutation(graphene.Mutation):
    class Arguments:
        input = CreateTaskInput(required=True)

    task = graphene.Field(TaskNode)

    @classmethod
    def mutate(cls, root, info, input=None):
        task_data = input
        task = Task(
            title=task_data.get('title'),
            description=task_data.get('description', ''),
            completed=task_data.get('completed', False)
        )
        task.save()
        return CreateTaskMutation(task=task)
    

class Query(graphene.ObjectType):
    task = relay.Node.Field(TaskNode)
    all_tasks = graphene.List(TaskNode)

    def resolve_all_tasks(root, info):
        return Task.objects.all()

class Mutation(graphene.ObjectType):
    create_task = CreateTaskMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
