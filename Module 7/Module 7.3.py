class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)
        self.all_words = self.get_all_words()

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ', '-', '—']
        for elem in self.file_names:
            with open(elem, 'r', encoding='utf-8') as file:
                lines = file.read().lower()
                for symbol in punctuation:
                    lines = lines.replace(symbol, '')
                    word = lines.split()
                    val = list(word)
                    all_words[elem] = val
        return all_words

    def find(self, word):
        word_ = word.lower()
        find_word = {}
        for name, words in self.all_words.items():
            if word_ in words:
                find_word[name] = words.index(word_) + 1
        return find_word

    def count(self, word):
        word_ = word.lower()
        quantity_word = {}
        for name, words in self.all_words.items():
            quantity_word[name] = words.count(word_)
        return quantity_word


finder1 = WordsFinder('Rudyard Kipling - If.txt',)

print(finder1.get_all_words())
print(finder1.find('if'))
print(finder1.count('if'))
