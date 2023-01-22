import calendar


class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

    @staticmethod
    def is_leap_year(year):
        """Проверяет, является ли год високосным"""
        ...  # TODO реализовать метод
        return calendar.isleap(year)

    @classmethod
    def get_max_day(cls, month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        ...  # TODO используя атрибут класса DAY_OF_MONTH вернуть количество дней в запрашиваемом месяце и году
        if cls.is_leap_year(year):
            return cls.DAY_OF_MONTH[1][month - 1]
        if not cls.is_leap_year(year):
            return cls.DAY_OF_MONTH[0][month - 1]



    def is_valid_date(self, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
        ...  # TODO проверить валидность даты
        if not isinstance(day, int) or not isinstance(month, int) or not isinstance(year, int):
            raise TypeError("Дата может быть только целым числом")
        if year <= 0:
            raise ValueError("Год должен быть больше 0")
        if not 0 < month <= 12:
            raise ValueError("Месяц не может иметь значение больше 12 и не может быть меньше 0")
        if not 0 < day <= self.DAY_OF_MONTH[0][month - 1]:
            raise ValueError(f"День должен быть больше нуля и не больше {self.DAY_OF_MONTH[0][month - 1]} ")


if __name__ == "__main__":
    date = Date(29, 11, 2020)
    print(Date.get_max_day(2,2000)) # Тут как я и хотел
    print(date.get_max_day) # не понимаю что это значит и почему я не могу вывести значение
    # (получаю <bound method Date.get_max_day of <class '__main__.Date'>>)
    print(date.get_max_day(2,2000)) # почему чтобы вывести значение надо опять вводить
    # параметры "месяц" и "год"? Ведь они же уже были введены, когда я создавал экземпляр "date" в 49 строке.
