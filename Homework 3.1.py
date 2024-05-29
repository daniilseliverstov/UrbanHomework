def single_root_words (root_word, *other_words):
    same_words = []
    for n in other_words:
        if root_word.lower() in n.lower() or n.lower() in root_word.lower():
            same_words.append(n)

    return same_words
print(single_root_words('rich','richiest, ', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
