import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides: int, filled=True):
        self.__sides = list(sides)
        self.__color = list(color)
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        param_color = [r, g, b]
        for value in param_color:
            if 0 <= value <= 255:
                return True
            else:
                return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *sides):
        for element in sides:
            if element > 0 and isinstance(element, int) and sides == self.__sides:
                return True
            else:
                return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        perimeter = sum(self.__sides)
        return perimeter

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = new_sides


class Circle(Figure):
    sides_count = 1

    def __radius(self):  # Не атрибут а метод?
        r = self.__len__() / (2 * math.pi)
        return r

    def get_square(self):
        return (math.pi * self.__radius()) ** 2


class Triangle(Figure):
    sides_count = 3

    def __calculate_height(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        base = max(a, b, c)
        return 2 * area / base

    def get_height(self):
        __height = self.__calculate_height
        return __height


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, *__sides, filled=True):
        super().__init__(__color, __sides, filled)


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
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
