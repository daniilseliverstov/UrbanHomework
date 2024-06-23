from random import randint, choice
class Building:
    total = 0
    def __init__(self):
        Building.total += 1

buildings = []
for i in range(40):
    buildings.append(Building())
print(buildings)
print(Building.total)
