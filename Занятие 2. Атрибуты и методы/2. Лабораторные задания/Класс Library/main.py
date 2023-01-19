from typing import Optional

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    """Класс книга"""

    def __init__(self, id_: int, name: str, pages: int):
        """
        Подготовка к работе и инициализация
        :param id_: идентификационный номер книги
        :param name: название книги
        :param pages: количество страниц
        """
        self.id_ = None
        self.name = None
        self.pages = None
        self.init_id(id_)
        self.init_name(name)
        self.init_pages(pages)

    def init_id(self, id_: int):
        """
        Инициализация атрибута id_
        :param id_: идентификационный номер книги
        """
        if not isinstance(id_, int):
            raise TypeError("ID должен быть целым числом")
        if id_ <= 0:
            raise ValueError("ID должен быть больше нуля")
        self.id_ = id_

    def init_name(self, name):
        """
        Инициализация атрибута name
        :param name: название книги
        """
        if not isinstance(name, str):
            raise TypeError("Название книги может быть только типа str")
        self.name = name

    def init_pages(self, pages):
        """
        Инициализация атрибута pages
        :param pages: количество страниц
        """
        if not isinstance(pages, int):
            raise TypeError("Количество страниц может быть тольок целым числом")
        if pages <= 0:
            raise ValueError("Количество страниц не может быть меньше нуля")
        self.pages = pages

    def __str__(self):
        """
        Строковое предстваление объекта
        :return: Строковое предстваление объекта
        """
        return f'Книга "{self.name}"'

    def __repr__(self):
        """
        Метод repr для класса Book
        :return: Возвращает название класса со всеми значениями его атрибутов
        """
        return f"{self.__class__.__name__}(id_={self.id_!r}, " \
               f"name={self.name!r}, pages={self.pages!r})"


# TODO написать класс Library
class Library:
    """
    Класс библиотека
    """
    start_book_id = 1

    def __init__(self, books: Optional = None):
        """
        Подготовка к работе и инициализация
        :param books: Список книг
        """
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        """
        Получение следующего свободного id
        :return: следующий свободный id для новой книги
        """
        if not self.books:
            return Library.start_book_id
        else:
            return self.books[-1].id_ + 1

    def get_index_by_book_id(self, book_id: int):
        """
        Получение индекса в списке книг по id книги
        :param book_id: ID книги
        :return: Индекс в списке книг
        """
        if not isinstance(book_id, int):
            raise TypeError("ID может быть только целым числом")
        if book_id < 1:
            raise ValueError("ID не может быть меньше 1")
        num_book = enumerate(self.books, 0)
        for i in num_book:
            if book_id == i[1].id_:
                return i[0]
        else:
            raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки
    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
