def single_root_words(root_word,*other_words):
    #word = other_words.count(root_word)
    same_words = []
    for word in other_words:
        if word.upper() in root_word.upper() or root_word.upper() in word.upper() :
            same_words.append(word)
    return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

#def SingleRootWords(root_words, *other_words):
    #same_words = []
    #for word in other_words:
        #if word.lower() in root_words.lower() or root_words.lower() in word.lower():
           # same_words.append(word)
    #return same_words
#res1 = SingleRootWords('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
#res2 = SingleRootWords('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
#print(res2)
