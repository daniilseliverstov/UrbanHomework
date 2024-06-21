class Building:
    def __init__(self, numberOfFloors: int, buildingType: str):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType
    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

Building_1 = Building(5,'A')
Building_2 = Building(2, 'B')
print(Building_1==Building_2)
Building_3 = Building(1,'C')
Building_4 = Building(1, 'C')
print(Building_3==Building_4)
Building_5 = Building(1,'C')
Building_6 = Building(1, 'A')
print(Building_5==Building_6)


