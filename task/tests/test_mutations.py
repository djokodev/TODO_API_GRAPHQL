import pytest
from .mutations import CREATE_TASK_MUTATION

@pytest.mark.django_db
def test_create_task(query_client):
    variables = {
        "input": {
            "title": "New TestTask",
            "description": "This is a new TestTask",
            "completed": False
        }
    }

    response = query_client.execute(CREATE_TASK_MUTATION, variable_values=variables)
    
    assert 'errors' not in response
    assert response['data']['createTask']['task']['title'] == "New TestTask"