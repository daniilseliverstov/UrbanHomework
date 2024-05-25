def calculate_structure_sum(args):
    summa = 0
    if isinstance(args, int):
        return args
    elif isinstance(args, str):
        return len(args)
    elif isinstance(args, (tuple, list, set)):
        for element in args:
            summa += calculate_structure_sum(element)
    elif isinstance(args, dict):
        for key, value in args.items():
            summa += calculate_structure_sum(key)
            summa += calculate_structure_sum(value)
    elif isinstance(args, tuple):
        for element in args:
            summa += calculate_structure_sum(element)
        return summa







    return summa
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
print(calculate_structure_sum(data_structure))