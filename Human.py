class Human:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        # private data
        self.__salary = 12


class Student(Human):
    def __init__(self, name, age, debt: int):
        super().__init__(name, age)
        self.debt = debt


student = Student('Nur Islom', 21, 150_000_000)
print(student.name)


# Inheritance, Abstraction, Encapsulation, Polymorphism
