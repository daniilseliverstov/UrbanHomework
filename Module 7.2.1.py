def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
        byte_num = file.tell()
        file.write(string + '\n')
        num_string = len(strings_positions) + 1
        strings_positions[(num_string, byte_num)] = string
    return strings_positions
    file.close()


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)