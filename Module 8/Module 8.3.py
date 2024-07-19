class Car:
    def __init__(self, model, vin, number):
        self.model = model
        self.__vin = vin
        self.__is_valid_vin()
        self.number = number
        self.__is_valid_numbers()

    def __is_valid_vin(self):
        if not isinstance(self.__vin, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not 1000000 <= self.__vin <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True

    def __is_valid_numbers(self):
        if not isinstance(self.number, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(self.number) != 6:
            raise IncorrectCarNumbers('Hеверная длина номера')
        else:
            return True


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
