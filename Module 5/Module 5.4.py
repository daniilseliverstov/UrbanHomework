from random import randint, choice


class Building:
    total = 0

    def __init__(self):
        Building.total += 1
        self.NumberOfFloors = randint(1,20)
        self.BuildingType = choice(['Жилой дом', 'Школа', 'Офисное здание'])

    def __str__(self):
        return f'Здание: {self.BuildingType}, Кол-во этажей {self.NumberOfFloors}'


buildings = []
for i in range(40):
    buildings.append(Building())
for building in buildings:
    print(building)
print(buildings)
print(Building.total)
