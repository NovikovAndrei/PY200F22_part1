from typing import Union


class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self.author = author
        self.is_valid_name(self.name)

    def is_valid_name(self, name):
        if not isinstance(name, str):
            raise TypeError("Название может быть только типа str")
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    # @name.setter
    # def name(self, name: str):
    #     if not isinstance(name, str):
    #         raise TypeError("Название может быть только типа str")
    #     self.__name = name

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        if not isinstance(author, str):
            raise TypeError("Автор может быть только типа str")
        self.__author = author

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __str__(self) -> str:
        return f"{super().__str__()}, кол-во страниц: {self.pages}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Кол-во страниц может быть только целым положительным числом")
        if value < 1:
            raise ValueError("Кол-во страниц может быть только целым положительным числом")
        self._pages = value


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __str__(self) -> str:
        return f"{super().__str__()}, Продолжительность: {self.duration}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value: Union[int, float]):
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность может быть только положительным числом")
        if value <= 0:
            raise ValueError("Продолжительность может быть только положительным числом")
        self._duration = float(value)


if __name__ == "__main__":
    # a = PaperBook("LOtR", "Tolkien", 22)
    # b = AudioBook('HarryPotter', 'Joanne Rowling', 1)
    c = Book("HP", 'Joanne Rowling')

