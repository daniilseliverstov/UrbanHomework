class House:
    def __init__(self, NunbersOfFloors=0):
        self.NumbersOfFloors = NunbersOfFloors

    def setNewNumberOfFloors (self, floors):
        self.NumbersOfFloors = floors
        print('Атрибут изменился: ',self.NumbersOfFloors)

value = House()
value.setNewNumberOfFloors(10)
