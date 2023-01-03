from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        #  TODO инициализировать объект "Стакан"
        if isinstance(capacity_volume, (int, float)):
            self.capacity_volume = capacity_volume
        else:
            raise TypeError("capacity_volume должен быть int или float")

        if isinstance(occupied_volume, (int, float)):
            self.occupied_volume = occupied_volume
        else:
            raise TypeError("occupied_volume должен быть int или float")
        if occupied_volume > capacity_volume:
            raise ValueError("occupied_volume должен быть меньше capacity_volume ")

if __name__ == "__main__":
    ...  # TODO инициализировать два объекта типа Glass
    glass_1 = Glass(500, 350)
    print(glass_1.capacity_volume)
    print(glass_1.occupied_volume)

    # TODO попробовать инициализировать не корректные объекты
