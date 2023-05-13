# Создайте класс "Фрукт", который содержит информацию о наименовании и весе
# фрукта. Создайте классы "Яблоко" и "Апельсин", которые наследуются от класса
# "Фрукт" и содержат информацию о цвете.

class fruit:
    # constructor
    def __init__(self, name: str, weight: float):
        self.__name_fruit = name
        self.__weight_fruit = weight

    # destructor
    def __del__(self):
        pass


class apple(fruit):
    # constructor
    def __init__(self, name: str, weight: float, color: str):
        self.__name_fruit = name
        self.__weight_fruit = weight
        self.__color_apple = color

    # destructor
    def __del__(self):
        pass


class orange(fruit):
    # constructor
    def __init__(self, name: str, weight: float, color: str):
        self.__name_fruit = name
        self.__weight_fruit = weight
        self.__color_orange = color

    # destructor
    def __del__(self):
        pass