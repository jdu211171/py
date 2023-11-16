class SpaceAircraft:
    def __init__(self, model, height, fuel):
        self.__model = model
        self.__height = height
        self.__fuel = fuel

    def get_fuel(self):
        return self.__fuel

    def set_fuel(self, new_value):
        self.__fuel = new_value

    def launch(self, km=0):
        if self.get_fuel() >= 2:
            print('Rocket launched')
        else:
            print('There is no enough fuel to rocket to luch')
            return
        while km < self.get_fuel() // 2:
            self.set_fuel(self.get_fuel() - 1)
            km += 1
        print(f'Rocket went up to {km} kilometers')
        self.land(km)

    def land(self, km):
        print(f'Rocket is launching')
        while km >= 0:
            self.set_fuel(self.get_fuel() - 1)
            km -= 1
        print(f'Rocket launched successfully')


spacex = SpaceAircraft('SpaceX', 200, 90)

spacex.launch()
