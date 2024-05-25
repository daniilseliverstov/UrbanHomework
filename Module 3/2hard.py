n = int(input('введите число от 3 до 20: '))
numb = []
for i in range(1, n):
    for j in range(1, n):
        if n % (i + j) == 0:
         numb.append(i)
         numb.append(j)
print(numb)