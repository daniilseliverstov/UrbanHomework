list_ = [1, 2, 3]
ab = []
for i in list_:
    j = i * -1
    ab.append(j)
print(ab)
a = []  # Создаем пустой список

a: list[int] = [10, 20]
b: list[int] = [30, 40]
a.append(50)  # Добавляем значение в конец списка
b.insert(2, 60)  # Вставляем значение по определенному индексу
print(a, b)