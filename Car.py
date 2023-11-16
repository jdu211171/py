class Car:
    id = 0

    def __init__(self):
        Car.id += 1
        self.id = Car.id


car1 = Car()
car2 = Car()
print(car1.id, car2.id)

Car.id = 13  # won't affect previous objects
