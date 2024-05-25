class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):

        all_words = {}

        for elem in self.file_names:
            with open(elem, encoding='utf-8') as file:
                for string_ in elem:
                    

