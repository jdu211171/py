class MinuteConverter:
    def __init__(self, minutes):
        self.__minutes = minutes

    def get_minutes(self) -> int:
        return self.__minutes

    def to_hours(self) -> int:
        return self.get_minutes() // 60

    def to_days(self) -> int:
        return self.to_hours() // 24

    def to_seconds(self) -> int:
        return self.get_minutes() * 60


minutes = MinuteConverter(240)
print(minutes.to_seconds())
