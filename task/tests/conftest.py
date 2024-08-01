import pytest
from graphene.test import Client
from todo.schema import schema
from task.models import Task

@pytest.fixture
def query_client():
    return Client(schema)

@pytest.fixture
def create_task():
    def make_task(title, description, completed=False):
        return Task.objects.create(title=title, description=description, completed=completed)
    return make_task
