def get_matrix(n, m, value):
    matrix = []
    for _ in range(n):
        row = []
        for _ in range(m):
            row.append(value)
        matrix.append(row)
    return matrix

res1 = get_matrix(4, 5, 21)
res2 = get_matrix(8, 2, 13)
print(res1)
print(res2)