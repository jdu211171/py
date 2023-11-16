class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_height(self):
        return self.height

    def set_height(self, new_height):
        self.height = new_height

    def get_width(self):
        return self.width

    def set_width(self, new_width):
        self.width = new_width

    def get_area(self):
        return self.get_width() * self.get_height()

    def get_perimeter(self):
        return (self.get_height() + self.get_width()) * 2

    def get_info(self):
        return (f'height: {self.get_height()}\n'
                f'width: {self.get_width()}\n'
                f'area: {self.get_area()}\n'
                f'perimeter: {self.get_perimeter()}')

