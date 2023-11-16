class Employee:
    def __init__(self, id: int, first_name: str, last_name: str, salary: int):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_id(self):
        return self.id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_full_name(self):
        return f'{self.get_first_name()} {self.get_last_name()}'

    def get_salary(self):
        return self.salary

    def set_salary(self, new_salary):
        self.salary = new_salary

    def get_annual_salary(self):
        return self.get_salary() * 12

    def raise_salary(self, percent: int):
        self.set_salary(self.salary * (1 + (percent) / 100))
        self.get_salary()

    def to_string(self):
        return f'Employee[id={self.get_id()}, name={self.get_full_name()}, salary={self.get_salary()}]'
    