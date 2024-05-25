a = (int(input('введите число от 3 до 20 ')))
key = []
for b in range(1, 20):
    for c in range(1, 20):
        if a % (b + c) == 0  and b < c:
            key.append(b)
            key.append(c)
print(f"{a} - {key}")





