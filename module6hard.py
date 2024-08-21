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
        if not all(isinstance(side, int) and side > 0 for side in new_sides):
            return False
        elif len(new_sides) > self.sides_count > len(new_sides):
            print("Некорректное количество сторон")
            return self.list_of_sides
        elif len(new_sides) == 1:
            self.list_of_sides = list(new_sides) * self.sides_count
            return self.list_of_sides
        elif len(new_sides) == self.sides_count:
            self.list_of_sides = list(new_sides)
            return self.list_of_sides
        return True

    def get_sides(self):
        return self.list_of_sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            return self.list_of_sides

    def __len__(self):
        return sum(self.list_of_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, len_circle, color, filled=True):
        super().__init__(len_circle, color, filled)
        self.__radius = len_circle / (2 * math.pi)
        self.list_of_sides = [len_circle] * self.sides_count
        self.len_circle = len_circle

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, sides, color, filled=True):
        super().__init__(sides, color, filled)
        self.list_of_sides = [sides] * self.sides_count
        self.sides = sides

    def get_square(self):
        s = sum(self.list_of_sides) / 2
        return math.sqrt(s * (s - self.list_of_sides[0]) * (s - self.list_of_sides[1]) * (s - self.list_of_sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, len_side, filled=True):
        super().__init__(len_side, color, filled)
        self.list_of_sides = [len_side] * self.sides_count
        self.len_side = len_side

    """Делаем свой метод валидации для куба __is_valid_sides для куба, с учетом того, что при вызове метода set_sides, 
    нельзя задавать 12 разных значений длин сторон куба(стороны куба равны)"""

    def __is_cube_valid(self, *new_sides):
        if not all(isinstance(side, int) and side > 0 for side in new_sides):
            return False
        elif len(new_sides) > self.sides_count > len(new_sides):
            print("Некорректное количество сторон")
            return self.list_of_sides
        elif len(new_sides) == 1:
            self.list_of_sides = list(new_sides) * self.sides_count
            return self.list_of_sides
        elif len(new_sides) == self.sides_count:
            """Если ввели 12 разных значений, или 11 одинаковых и 1 отличающееся, то просто выводим лист из текущих
            сторон куба"""
            if len(set(new_sides)) != 1:
                return self.list_of_sides
        return True

    def set_sides(self, *new_sides):
        if self.__is_cube_valid(*new_sides):
            return self.list_of_sides

    def get_volume(self):
        return self.len_side ** 3


if __name__ == '__main__':
    """Создание объектов классов"""

    circle1 = Circle(10, (200, 200, 100))  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)
    triangle = Triangle(10, (200, 200, 100))

    """Проверка на изменение цветов"""

    print(f"Проверка на изменение цветов\n")
    circle1.set_color(55, 66, 77)  # Изменится
    triangle.set_color(55, 66, 77)
    cube1.set_color(300, 70, 15)  # Не изменится
    print(circle1.get_color())
    print(triangle.get_color())
    print(cube1.get_color())
    print()
    """Проверка на изменение сторон(Не изменится)"""

    print(f"Проверка на изменение сторон(Не изменится)\n")
    circle1.set_sides(5, 3, 12, 4, 5)
    triangle.set_sides(5, 3, 12, 4, 5)
    cube1.set_sides(5, 3, 12, 4, 5, 5, 3, 12, 4, 5, 2, 5)
    print(circle1.get_sides())
    print(cube1.get_sides())
    print(triangle.get_sides())
    print()

    """Проверка на изменение сторон(Изменится)\n"""

    print(f"Проверка на изменение сторон(Изменится)\n")
    circle1.set_sides(5)
    triangle.set_sides(5, 5, 5)
    cube1.set_sides(7)
    print(circle1.get_sides())
    print(triangle.get_sides())
    print(cube1.get_sides())
    print()

    """Проверка методов get_square"""

    print(f"Проверка методов get_square\n")
    print(triangle.get_square())
    print(circle1.get_square())
    print()

    """Проверка периметра (круга), это и есть длина"""

    print(f"Проверка периметра (круга), это и есть длина\n")
    print(len(circle1))
    print()

    """Проверка объёма (куба)"""

    print(f"Проверка объёма (куба)\n")
    print(cube1.get_volume())
