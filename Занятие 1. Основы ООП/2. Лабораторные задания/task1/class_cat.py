# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Cat:
    def __init__(self, breed: str, name: str, fluffiness: str, age: int, character: str):
        """
        Создание и подготовка к работе объекта "кот"
        :param breed: порода
        :param name: кличка
        :param fluffiness: пушистость
        :param age: возраст
        :param character: тип характера

        Примеры:
        >>> hulk = Cat('Main-coon', 'hulk', 'longhaired', 10, 'calm')
        >>> hulk.breed
        'Main-coon'
        >>> hulk.name
        'Hulk'
        >>> hulk.fluffiness
        'longhaired'
        >>> hulk.age
        10
        >>> hulk.character
        'calm'

        """
        self.breed = None
        self.name = None
        self.fluffiness = None
        self.age = None
        self.character = None
        self.init_breed(breed)
        self.init_name(name)
        self.init_fluffiness(fluffiness)
        self.init_age(age)
        self.init_character(character)

    def init_breed(self, breed: str):
        """
        Инициализация атрибута breed
        :param breed: порода
        :return: название породы
        """
        if not isinstance(breed, str):
            raise TypeError('"breed" должен быть типа "str"')
        self.breed = breed

    def init_name(self, name: str):
        """
        Инициализация атрибута name
        :param name: кличка
        :return: кличка
        """
        if not isinstance(name, str):
            raise TypeError('"name" должен быть типа "str"')
        self.name = name.capitalize()

    def init_fluffiness(self, fluffiness: str):
        """
        Инициализация атрибута fluffiness
        :param fluffiness: пушистость
        :return: тип пушистости
        """
        if fluffiness not in ('bald', 'smooth-haired', 'medium-haired', 'longhaired'):
            raise ValueError('"fluffiness" может быть только: "bald", '
                             '"smooth-haired", "medium-haired", "longhaired" ')
        self.fluffiness = fluffiness

    def init_age(self, age: int):
        """
        Инициализация атрибута age
        :param age: возраст
        :return: текущий возраст
        """
        if not isinstance(age, int):
            raise TypeError('"age" может быть только целым числом (int)')
        if not age > 0:
            raise ValueError('"age" не может быть отрицательным')
        self.age = age

    def init_character(self, character: str):
        """
        Инициализация атрибута character
        :param character: характер
        :return: характер
        """
        if character not in ("calm", "moderate", "active"):
            raise ValueError('"character" может быть только: "calm", "moderate", "active"')
        self.character = character

    def add_age(self, increase_age: int):
        """
        Увеличение возраста на заданную величину
        :param increase_age: на сколько лет увеличиваем возраст
        :return: новый текущий возраст

        Примеры:
        >>> hulk = Cat('Main-coon', 'hulk', 'longhaired', 10, 'calm')
        >>> hulk.add_age(5)
        >>> hulk.age
        15
        """
        if increase_age <= 0:
            raise ValueError('"increase_age" должен быть больше нуля')
        self.age += increase_age

    def change_character(self, new_character: str):
        """
        Смена типа характера
        :param new_character: новый тип характера
        :return: новый текущий тип характера

        Примеры:
        >>> hulk = Cat('Main-coon', 'hulk', 'longhaired', 10, 'calm')
        >>> hulk.change_character('active')
        >>> hulk.character
        'active'
        """
        if new_character not in ("calm", "moderate", "active"):
            raise ValueError('"character" может быть только: "calm", "moderate", "active"')
        if self.character == new_character:
            raise ValueError('"character" должен отличаться от "new_character"')
        self.character = new_character

    def __repr__(self) -> str:
        """
        Метод repr для создания копии объекта класса
        :return: объект класса Cat со всеми атрибутами
        """
        return f"Cat({self.breed}, {self.name}, {self.fluffiness}, {self.age}, {self.character})"


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
