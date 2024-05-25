def print_params(a = 5, b = 'word', c = True):
    print(a, b, c)

print_params(8, 3)
print_params(1, 25, [1, 2, 3] )

values_list = [78, 'wert', True]
values_dict = {'a': 4, 'b': '1234', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2,17)