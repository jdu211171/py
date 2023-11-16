class Student:
    def __init__(self, name: str):
        self.name = name

    def return_name(self):
        return self.name

    def greet(self):
        return 'Assalom...'


class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
