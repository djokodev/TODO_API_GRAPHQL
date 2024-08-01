CREATE_TASK_MUTATION = """
mutation CreateTask($input: CreateTaskInput!) {
  createTask(input: $input) {
    task {
      id
      title
      description
      completed
    }
  }
}
"""
