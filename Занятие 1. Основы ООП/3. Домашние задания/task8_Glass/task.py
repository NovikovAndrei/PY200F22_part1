# TODO Добавить методы add_water и remove_water
from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = None
        self.occupied_volume = None
        self.init_capacity_volume(capacity_volume)
        self.init_occupied_volume(occupied_volume)

    def init_capacity_volume(self, capacity_volume):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if not capacity_volume > 0:
            raise ValueError
        self.capacity_volume = capacity_volume  # объем стакана

    def init_occupied_volume(self, occupied_volume):
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError
        self.occupied_volume = occupied_volume  # объем жидкости в стакане

    def add_water(self, new_water: Union[int, float]):
        if not isinstance(new_water, (int, float)):
            raise TypeError
        if new_water < 0:
            raise ValueError
        if new_water + self.occupied_volume > self.capacity_volume:
            raise ValueError("нельзя наливать больше capacity_volume")
        self.occupied_volume += new_water

    def remove_water(self, rem_water: Union[int, float]):
        if not isinstance(rem_water, (int, float)):
            raise TypeError
        if rem_water < 0:
            raise ValueError
        if rem_water > self.occupied_volume:
            raise ValueError("нельзя вылить больше occupied_volume")
        self.occupied_volume -= rem_water



if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса
    print(glass.capacity_volume, glass.occupied_volume)
    glass.add_water(11)
    print(glass.occupied_volume)
    glass.remove_water(22)
    print(glass.occupied_volume)