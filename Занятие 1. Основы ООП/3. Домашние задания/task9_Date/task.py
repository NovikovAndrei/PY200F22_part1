# TODO class Date

class Date:

    def __init__(self, day: int, month: int, year: int):
        self.day = None
        self.month = None
        self.year = None
        self.init_day(day)
        self.init_month(month)
        self.init_year(year)

    def init_day(self, day: int):
        if not isinstance(day, int):
            raise TypeError("день должен быть целым числом")
        self.day = day

    def init_month(self, month: int):
        if not isinstance(month, int):
            raise TypeError("месяц должен быть целым числом")
        self.month = month

    def init_year(self, year: int):
        if not isinstance(year, int):
            raise TypeError("год должен быть целым числом")
        self.year = year

    def __repr__(self):
        return f'Date({self.day}, {self.month}, {self.year})'

    def __str__(self):
        return f'{str(self.day).rjust(2,"0")}/{str(self.month).rjust(2,"0")}/{str(self.year).rjust(4, "0")}'

if __name__ == "__main__":
    date = Date(9, 1, 1989)
    print(date.day)
    print(date.__repr__())
    print(date)


