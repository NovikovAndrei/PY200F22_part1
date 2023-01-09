from typing import Union
import doctest


class Cinema:
    def __init__(self, title: str, genre: str, budget: Union[int, float],
                 total_box_office: Union[int, float], weeks: int):
        """
        Создание и подготовка к работе класса "Фильм"
        :param title: Название фильма
        :param genre: Жанр
        :param budget: Бюджет фильма
        :param total_box_office: общие сборы фильма в прокате
        :param weeks: количество недель в прокате

        Примеры:
        >>> cinema1 = Cinema('avatar', 'fantasy', 200, 0, 0)
        >>> cinema1.title
        'Avatar'
        >>> cinema1.genre
        'fantasy'
        >>> cinema1.budget
        200
        >>> cinema1.total_box_office
        0
        >>> cinema1.weeks
        0
        """
        self.title = None
        self.genre = None
        self.budget = None
        self.total_box_office = None
        self.weeks = None
        self.init_title(title)
        self.init_genre(genre)
        self.init_budget(budget)
        self.init_total_box_office(total_box_office)
        self.init_weeks(weeks)

    def init_title(self, title):
        """
        Инициализация атрибута title
        :param title: название фильма
        """
        if not isinstance(title, str):
            raise TypeError('"title" может быть только типа "int"')
        self.title = title.capitalize()

    def init_genre(self, genre):
        """
        Инициализация атрибута genre
        :param genre: жанр фильма
        """
        if genre not in ("action", "comedy", "fantasy", "horror"):
            raise ValueError('"genre" может быть только: "action", "comedy", "fantasy", "horror"')
        self.genre = genre

    def init_budget(self, budget):
        """
        Инициализация атрибута budget
        :param budget: бюджет фильма
        """
        if not isinstance(budget, (int, float)):
            raise TypeError('"budget" может быть только типа "int/float"')
        if budget <= 0:
            raise ValueError('"budget" должен быть больше нуля')
        self.budget = budget

    def init_total_box_office(self, total_box_office):
        """
        Инициализация атрибута total_box_office
        :param total_box_office: общие сборы фильма
        """
        if not isinstance(total_box_office, (int, float)):
            raise TypeError('"total_box_office" может быть только типа "int/float"')
        if total_box_office != 0:
            raise ValueError('при инициализации нового фильма "total_box_office" всегда ноль')
        self.total_box_office = total_box_office

    def init_weeks(self, weeks):
        """
        Инициализация атрибута weeks
        :param weeks: количество недель в прокате
        """
        if not isinstance(weeks, int):
            raise TypeError('"weeks" может быть только типа "int"')
        if weeks != 0:
            raise ValueError('при инициализации нового фильма "weeks" всегда ноль')
        self.weeks = weeks

    def add_week_results(self, current_box_office):
        """
        Добавление результатов за неделю и сохранение их в файле
        :param current_box_office: сборы за текущую неделю
        """
        if not isinstance(current_box_office, (int, float)):
            raise TypeError('"current_box_office" может быть только типа "int/float"')
        if current_box_office < 0:
            raise ValueError('"current_box_office" не может быть меньше нуля')
        self.weeks += 1
        self.total_box_office += current_box_office
        with open('result.txt', 'a', encoding='utf8') as f:
            f.writelines(f'\tРезультат за неделю - {self.weeks}\n'
                         f'{current_box_office} - сборы за текущую неделю\n'
                         f'{self.total_box_office} - общая сумма сборов\n'
                         f'{self.get_current_payback()} - окупаемость на текущую неделю\n ')

    def get_current_payback(self):
        """
        Расчитывает текущую окупаемость фильма
        :return: текущая окупаемость фильма в процентах

        Примеры:
        >>> cinema1 = Cinema('avatar', 'fantasy', 200, 0, 0)
        >>> cinema1.add_week_results(10)
        >>> cinema1.get_current_payback()
        '5%'
        """
        return f'{int((self.total_box_office / self.budget) * 100)}%'


if __name__ == "__main__":
    doctest.testmod()
    # cinema1 = Cinema('avatar', 'fantasy', 200, 0, 0)
    # print(cinema1.title)
    # print(cinema1.total_box_office)
    # print(cinema1.weeks)
    # cinema1.add_week_results(10)
    # print(cinema1.get_current_payback())
    # cinema1.add_week_results(10)
    # print(cinema1.get_current_payback())
    # cinema1.add_week_results(300)
    # print(cinema1.get_current_payback())
    # print(cinema1.weeks)
