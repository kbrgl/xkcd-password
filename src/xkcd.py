import os.path
from random import randint


class XkcdPasswordGenerator:
    """generates xkcd-inspired passwords"""
    def __init__(self, word_list):
        self.word_list = word_list

    def generate(self, words=4, separator=' '):
        result = [self.random_word() for _ in range(words)]
        if separator is not None:
            return separator.join(result)
        else:
            return result

    def random_word(self):
        return self.word_list[randint(0, (len(self.word_list) - 1))]


if __name__ == '__main__':
    with open('dictionary.csv') as f:
        generator = XkcdPasswordGenerator([line for line in f.read().split(',')])
    print(generator.generate())
