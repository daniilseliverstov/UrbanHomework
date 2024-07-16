import math


class Figure:
    sides_count = 0

    def __init__(self, color: tuple, *sides: int, filled: bool = True):
        if len(sides) != self.sides_count:
            self.__sides = [1*self.sides_count]
        else:
            self.__sides = [i for i in sides]
        self.__color = color
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
        cond1 = len(sides) == 1
        cond2 = all([isinstance(side, int) and side > 0 for side in sides])
        return cond1 and cond2


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

    def get_radius(self):  # Не атрибут а метод?
        r = self.__len__() / (2 * math.pi)
        return r

    def get_square(self):
        return (math.pi * self.get_radius()) ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color: tuple, *sides):
        super().__init__(color, *sides)

    def __calculate_height(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        base = max(a, b, c)
        return 2 * area / base

    def get_height(self):
        __height = self.__calculate_height
        return __height

    def get_square(self):
        a, b, c = self.get_sides()
        p = sum(self.get_sides()) / 2
        s = (p * (p - self.get_sides()[a])) * (p - self.get_sides()[b]) * (p - self.get_sides()[c]) ** 0.5
        return s


class Cube(Figure):
    sides_count = 12

    def __init__(self, color,  *sides: int, filled: bool = True):
        super().__init__(color, *sides, filled)
        if len(sides) == 1:
            self.__sides = self.sides_count*[i for i in sides]
        else:
            self.__sides = [1*self.sides_count]

    def get_sides(self):
        return [*self.__sides]

    def get_volume(self):
        return self.__sides[1]**3


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


