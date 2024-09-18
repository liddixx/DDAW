
This class manages a list of students and their grades.
It includes methods to:
1. Add a new student with their grade.
2. Remove an existing student by their name.
3. Update the grade of an existing student.
4. Show the list of all students with their grades.
5. Search for the grade of a specific student.


```python
class StudentManager:
    def __init__(self):
        """Initializes the StudentManager with an empty list of students."""
        self.students = []

    def add_student(self, name, grade):
        """Adds a new student with their grade to the list."""
        pass

    def remove_student(self, name):
        """Removes a student from the list by their name."""
        pass

    def update_grade(self, name, new_grade):
        """Updates the grade of an existing student."""
        pass

    def show_students(self):
        """Shows the list of all students with their grades."""
        pass

    def search_grade(self, name):
        """Searches and shows the grade of a student by their name."""
        pass

# Example usage of the StudentManager class
if __name__ == "__main__":
    manager = StudentManager()
    # Example calls to methods (to be implemented)
    manager.add_student("Ana", 85)
    manager.add_student("Luis", 90)
    manager.show_students()
    manager.update_grade("Ana", 88)
    manager.search_grade("Luis")
    manager.remove_student("Luis")
    manager.show_students()
```
