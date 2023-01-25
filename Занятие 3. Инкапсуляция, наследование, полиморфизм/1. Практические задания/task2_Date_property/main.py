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

        self.is_valid_date(self._day, self._month, self._year)

    # TODO какой декоратор следует применить?
    @staticmethod
    def is_leap_year(year: int) -> bool:
        """Проверяет, является ли год високосным"""
        # TODO записать условие проверки високосного года
        return calendar.isleap(year)

    @classmethod
    def get_max_day(cls, month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        ...  # TODO используя атрибут класса DAY_OF_MONTH вернуть количество дней в запрашиваемом месяце и году
        if cls.is_leap_year(year):
            return cls.DAY_OF_MONTH[1][month - 1]
        if not cls.is_leap_year(year):
            return cls.DAY_OF_MONTH[0][month - 1]

    def is_valid_date(self, day: int, month: int, year: int) -> bool:
        """Проверяет, является ли дата корректной"""
        # TODO если указанный набор день, месяц и год неверны, то вызвать ошибку ValueError
        if not isinstance(day, int) or not isinstance(month, int) or not isinstance(year, int):
            raise TypeError("Дата может быть только целым числом")
        if year <= 0:
            raise ValueError("Год должен быть больше 0")
        if not 0 < month <= 12:
            raise ValueError("Месяц не может иметь значение больше 12 и не может быть меньше 0")
        if not 0 < day <= self.get_max_day(month, year):
            raise ValueError(f"День должен быть больше нуля и не больше {self.DAY_OF_MONTH[1][month - 1]}")
        return True

    # TODO записать getter и setter для дня
    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        if 0 < value < 32:
            self._day = value
        else:
            raise ValueError("ошибка из day getter")

    # TODO записать getter и setter для месяца
    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        if 0 < value < 13:
            self._month = value
        else:
            raise ValueError("ошибка из month setter")

    # TODO записать getter и setter для года
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise ValueError("ошибка из year setter")
        if value < 1:
            raise ValueError("ошибка из year setter")
        self._year = value


if __name__ == "__main__":
    d = Date(28, 14, 2001)
