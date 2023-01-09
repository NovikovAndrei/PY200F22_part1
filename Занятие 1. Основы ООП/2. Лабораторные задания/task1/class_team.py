from typing import Union
import doctest


class FootballTeam:
    def __init__(self, name: str, colour: str, league: str, rank: Union[str, int]):
        """
        Создание и подготовка к работе класса "Футбольная команда"
        :param name: название команды
        :param colour: клубные цвета команды
        :param league: лига в которой играет команда
        :param rank: место в чемпионате

        Примеры:
        >>> team1 = FootballTeam('liverpool', 'red', 'Premier League', 2)
        >>> team1.name
        'Liverpool'
        >>> team1.colour
        'red'
        >>> team1.league
        'Premier League'
        >>> team1.rank
        2
        """
        self.name = None
        self.colour = None
        self.league = None
        self.rank = None
        self.init_name(name)
        self.init_colour(colour)
        self.init_league(league)
        self.init_rank(rank)

    def init_name(self, name: str):
        """
        Инициализация атрибута "название команды"
        :param name: Название команды
        :return: название команды
        """
        if not isinstance(name, str):
            raise TypeError('"name" может быть только типа "str"')
        self.name = name.capitalize()

    def init_colour(self, colour: str):
        """
        Инициализация атрибута "клубные цвета"
        :param colour: клубные цвета
        :return: клубные цвета
        """
        if not isinstance(colour, str):
            raise TypeError('"colour" может быть только типа "str"')
        self.colour = colour

    def init_league(self, league: str):
        """
        Инициализация атрибута "Лига"
        :param league: Лига в которой играет команда
        :return: Лига в которой играет команда
        """
        if league not in ("Premier League", "EFL Championship", "EFL League One", "EFL League Two", "National League"):
            raise ValueError('"league" может быть только: "Premier League", '
                             '"EFL Championship", "EFL League One", "EFL League Two", "National League"')
        self.league = league

    def init_rank(self, rank: Union[str, int]):
        """
        Инициализация атрибута "место в чемпионате"
        :param rank: место которое занимает команда в чемпионате
        :return: место которое занимает команда в чемпионате
        """
        if not isinstance(rank, (int, str)):
            raise TypeError('"rank" может быть только типа "int" в диапазоне 2-20 или "champion"')
        if isinstance(rank, str):
            if rank != "champion":
                raise ValueError('"rank" может быть только типа "int" в диапазоне 2-20 или "champion"')
        if isinstance(rank, int):
            if not 1 < rank < 20:
                raise ValueError('"rank" может быть только типа "int" в диапазоне 2-20 или "champion"')
        self.rank = rank

    def change_league(self, new_league: str):
        """
        Смена лиги в кторой играет команда
        :param new_league: новая лига в которой будет играть команда
        :return: новая лига в которой будет играть команда

        Примеры:
        >>> team1 = FootballTeam('liverpool', 'red', 'Premier League', 2)
        >>> team1.change_league('EFL Championship')
        >>> team1.league
        'EFL Championship'
        """
        if new_league not in (
                "Premier League", "EFL Championship", "EFL League One", "EFL League Two", "National League"):
            raise ValueError('"league" может быть только: "Premier League", '
                             '"EFL Championship", "EFL League One", "EFL League Two", "National League"')
        if self.league == new_league:
            raise ValueError('"new_league" должен отличаться от "league"')
        self.league = new_league

    def change_rank(self, new_rank: Union[str, int]):
        """
        Смена места в турнирной таблице чемпионата
        :param new_rank: новое место в турнирной таблице чемпионата
        :return: новое место в турнирной таблице чемпионата

        Примеры:
        >>> team1 = FootballTeam('liverpool', 'red', 'Premier League', 2)
        >>> team1.change_rank('champion')
        >>> team1.rank
        'champion'
        """
        if not isinstance(new_rank, (int, str)):
            raise TypeError('"new_rank" может быть только типа "int" в диапазоне 2-20 или "champion"')
        if isinstance(new_rank, str):
            if new_rank != "champion":
                raise ValueError('"new_rank" может быть только типа "int" в диапазоне 2-20 или "champion"')
        if isinstance(new_rank, int):
            if not 1 < new_rank < 20:
                raise ValueError('"new_rank" может быть только типа "int" в диапазоне 2-20 или "champion"')
        if self.rank == new_rank:
            raise ValueError('"new_rank" должен отличаться от "rank"')
        self.rank = new_rank

    def __repr__(self) -> str:
        """
        Метод repr для создания копии объекта класса
        :return: объект класса футбольная команда со всеми атрибутами класса

        Примеры:
        >>> team1 = FootballTeam("arsenal", "red-white", "Premier League", 5)
        >>> team1.__repr__()
        'FootballTeam(Arsenal, red-white, Premier League, 5)'
        """
        return f"FootballTeam({self.name}, {self.colour}, {self.league}, {self.rank})"

    def __str__(self):
        """
        Метод str для распечатки объекта класса "футбольная команда"
        :return: объект класса футбольная команда со всеми атрибутами класса

        Примеры:
        #>>> team1 = FootballTeam("arsenal", "red-white", "Premier League", 5)
        #>>> team1.__str__()
        #'Название: "Arsenal"\nКлубный цвет: "red-white"\nЛига: "Premier League"\nМесто в чемпионате: 5'
        """
        return f'Название: "{self.name}"\nКлубный цвет: "{self.colour}"\n' \
               f'Лига: "{self.league}"\nМесто в чемпионате: {self.rank}'


if __name__ == "__main__":
    doctest.testmod()

