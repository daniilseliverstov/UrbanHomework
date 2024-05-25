class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if self.number_of_floors > new_floor:
            for num_floor in range(1, new_floor+1):
                print(f'В доме {self.name} можно доехать на {num_floor} этаж')
        else:
            print(f'Нет такого этажа в "{self.name}"')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
