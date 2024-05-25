#1
def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
print_params()
print_params(9)
print_params(9,'string')
print_params(c = False)
print_params(b = 25)
print_params(c = [1,2,3])

#2
values_list = [8, 'june', True]
values_dict = {'a': 9, 'b': 'июнь', 'c': False}
print_params(*values_list)
print_params(**values_dict)

#3
values_list_2 = [8,'june']
print_params(*values_list_2, 2024)