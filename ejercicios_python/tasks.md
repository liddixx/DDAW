# Task Management Exercise

This exercise focuses on managing a list of tasks, where each task has a title and a priority (e.g., "high", "medium", "low").

## Requirements:

1. Add a task with its priority.
2. Remove a task by its title.
3. Update the priority of an existing task.
4. Display the list of all tasks with their priorities.
5. Search for the priority of a specific task.

## Skeleton:
```python
class TaskManager:
    def __init__(self):
        """Initializes the class with an empty list of tasks."""
        self.tasks = []

    def add_task(self, title, priority):
        """Adds a new task with its priority (high/medium/low)."""
        pass

    def remove_task(self, title):
        """Removes a task from the list by its title."""
        pass

    def update_priority(self, title, new_priority):
        """Updates the priority of an existing task."""
        pass

    def show_tasks(self):
        """Displays the complete list of tasks and their priorities."""
        pass

    def search_priority(self, title):
        """Searches for the priority of a specific task."""
        pass

# Example usage
if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.add_task("Clean the house", "high")
    task_manager.add_task("Do the shopping", "medium")
    task_manager.show_tasks()
    task_manager.update_priority("Clean the house", "low")
    task_manager.search_priority("Do the shopping")
    task_manager.remove_task("Do the shopping")
    task_manager.show_tasks()
```
