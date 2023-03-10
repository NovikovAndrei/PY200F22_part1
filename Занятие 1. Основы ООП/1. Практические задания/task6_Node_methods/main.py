from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        # TODO добавить атрибуты
        self.value = value
        self.next_ = next_

    def get_value(self) -> Any:
        """Метод, который возвращает значение атрибута value"""
        ...  # TODO вернуть значение узла
        return self.value

    # TODO добавить метод get_next
    def get_next(self,) -> Any:
        return self.next_

    def __repr__(self):
        return f"Node({self.value}, {self.next_})"

if __name__ == '__main__':
    #first_node = Node(1)  # первый узел
    #second_node = Node(2)  # второй узел

    t1 = Node(1)
    t2 = Node(2, t1)
    t3 = Node(3, t2)
    t4 = Node(4, t3)
    print(t4)
    print(t4.get_next())
    print(t4.get_next().get_value())
    # TODO с помощью метода распечатать значение первого узла
    # TODO  с помощью метода распечатать следующий узел второго узла
