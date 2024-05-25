 #Работа со списками:
 # - Создайте переменную my_list и присвойте ей список из нескольких элементов, например, фруктов.
 # - Выведите на экран список my_list.
#  - Выведите на экран первый и последний элементы списка my_list.
 # - Выведите на экран подсписок my_list с третьего до пятого элементов.
#  - Измените значение третьего элемента списка my_list.
#  - Выведите на экран измененный список my_list.

#3. Работа со словарями:
#  - Создайте переменную my_dict и присвойте ей словарь с парами ключ-значение, например, переводами некоторых слов.
#  - Выведите на экран словарь my_dict.
#  - Выведите на экран значение для заданного ключа в my_dict.
#  - Измените значение для заданного ключа или добавьте новый в my_dict.
#  - Выведите на экран измененный словарь my_dict.
my_list = ['circle', 'triangle', 'square', 'oval', 'diamond']
print(my_list)
print(my_list[0], my_list[-1])
print(my_list[2:5])
my_list[2] = 'cube'
print(my_list)

my_dict = {'circle': 'круг', 'triangle': 'треугольник', 'square': 'квадрат', 'oval': 'овад', 'diamond':'ромб'}
print(my_dict)
print(my_dict['square'])
my_dict.update({'cube': 'куб'})
print('обновленный словарь:', my_dict)
my_dict['circle'] = 'KRUG'
print('измененный словарь:', my_dict)
