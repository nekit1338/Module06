import math


class Figure:
    sides_count = 0

    def __init__(self, sides: int, color, filled: True):
        self.__sides = sides
        self.__color = color
        self.filled = filled
        self.list_of_sides = []

    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            return False

        for side in new_sides:
            if not isinstance(side, int) or side <= 0:
                return False

        return True

    def get_sides(self):
        return self.list_of_sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.list_of_sides = list(new_sides)

    def __len__(self):
        return sum(self.list_of_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, len_circle, color, filled=True):
        super().__init__(len_circle, color, filled)
        self.__radius = len_circle / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, sides, color, filled=True):
        super().__init__(sides, color, filled)

    def get_square(self):
        s = sum(self.list_of_sides) / 2
        return math.sqrt(s * (s - self.list_of_sides[0]) * (s - self.list_of_sides[1]) * (s - self.list_of_sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, len_side, filled=True):
        super().__init__(len_side, color, filled)
        self.list_of_sides = [len_side] * 12
        self.len_side = len_side

    def get_volume(self):
        return self.len_side ** 3


if __name__ == '__main__':

    circle1 = Circle(10, (200, 200, 100))  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())
