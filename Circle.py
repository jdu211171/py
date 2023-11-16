import math


class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        self.color = new_color

    def get_area(self):
        return math.pow(self.get_radius(), 2) * math.pi

    def get_circumference(self):
        return self.get_radius() * 2 * math.pi

    def get_info(self):
        return (f'radius: {self.get_radius()}\n'
                f'color: {self.get_color()}\n'
                f'area: {self.get_area()}\n'
                f'circumference: {self.get_circumference()}')
