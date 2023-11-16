class Organism:
    def __init__(self, is_alive: bool):
        self.is_alive = is_alive

    def get_is_alive(self):
        return self.is_alive

    def set_is_alive(self):
        self.is_alive = not self.get_is_alive()
        print(f"Now this cell is {'dead' if self.is_alive else 'alive'}")

    def info(self):
        return f'is this organism alive? {self.get_is_alive()}'


class Cell(Organism):
    def __init__(self, is_alive: bool, type: str):
        super().__init__(is_alive)
        self.type = type

    def get_type(self):
        return self.type

    def set_type(self, new_type):
        self.type = new_type

    def info(self):
        return f'Cell type: {self.get_type()}, {super().info()}'


cell = Cell(True, 'parasite')
cell.set_is_alive()
cell.set_is_alive()

