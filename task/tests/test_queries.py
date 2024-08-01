import pytest
from .queries import ALL_TASKS_QUERY


@pytest.mark.django_db
def test_all_tasks(query_client, create_task):
    create_task(title="Task 1", description="Description 1")
    create_task(title="Task 2", description="Description 2")
    
    response = query_client.execute(ALL_TASKS_QUERY)
    
    assert 'errors' not in response
    assert len(response['data']['allTasks']) == 2
    assert response['data']['allTasks'][0]['title'] == "Task 1"
    assert response['data']['allTasks'][1]['title'] == "Task 2"