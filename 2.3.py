my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
new_list = []
while i < len(my_list):
    if my_list[i] >= 0:
        new_list.append(my_list[i])
        i += 1
        if my_list[i] == 0:
            i += 1
        continue
    else:
        break
print(new_list)