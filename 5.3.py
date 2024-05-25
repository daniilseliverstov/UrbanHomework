class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __eq__(self, other):
        isinstance(other.number_of_floors, int)
        isinstance(self.number_of_floors, int)
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        isinstance(other.number_of_floors, int)
        isinstance(self.number_of_floors, int)
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        return self.number_of_floors + value

    def __iadd__(self, value):
        return self.number_of_floors + value

    def __radd__(self, value):
        return self.number_of_floors + value



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(f'Наименование: {h1.name}, Количество этажей: {h1.number_of_floors}')
print(f'Наименование: {h2.name}, Количество этажей: {h2.number_of_floors}')

print(f'{h1.name} равен {h2.name}: {h1 == h2}') # __eq__

h1.number_of_floors = h1.number_of_floors + 10 # __add__
print(f'Наименование: {h1.name}, Количество этажей: {h1.number_of_floors}')
print(f'{h1.name} равен {h2.name}: {h1 == h2}')

h1.number_of_floors += 10 # __iadd__
print(f'Наименование: {h1.name}, Количество этажей: {h1.number_of_floors}')

h2.number_of_floors = 10 + h2.number_of_floors # __radd__
print(f'Наименование: {h2.name}, Количество этажей: {h2.number_of_floors}')

print(f'{h1.name} больше {h2.name}: {h1 > h2}') # __gt__
print(f'{h1.name} больше либо равен {h2.name}: {h1 >= h2}') # __ge__
print(f'{h1.name} меньше {h2.name}: {h1 < h2}') # __lt__
print(f'{h1.name} меньше либо равен {h2.name}: {h1 <= h2}') # __le__
print(f'{h1.name} не равен {h2.name}: {h1 != h2}') # __ne__

