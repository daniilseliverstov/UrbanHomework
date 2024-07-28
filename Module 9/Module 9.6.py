def all_variants(text):
    for categorias_figuras in range(1, len(text) + 1):
        for segmentum in range(len(text) - categorias_figuras + 1):
            yield text[segmentum:(segmentum + categorias_figuras)]


a = all_variants("abc")
for i in a:
    print(i)
