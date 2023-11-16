import datetime
class Date:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def get_day(self):
        return self.day

    def get_month(self):
        return self.month

    def get_year(self):
        return self.year

    def set_day(self, new_day):
        self.day = new_day

    def set_month(self, new_month):
        self.month = new_month

    def set_year(self, new_year):
        self.year = new_year

    def set_date(self, day: int, month: int, year: int):
        self.set_day(day)
        self.set_month(month)
        self.set_year(year)

    def to_string(self):
        return datetime.datetime(self.year, self.month, self.day).strftime('%d/%m/%Y')


date = Date(4, 2, 2023)
print(date.to_string())