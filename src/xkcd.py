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


def parse(file, delimiter=","):
    """
    splits the contents of file at delimiter
    :param delimiter: the delimiter by which words in word list are separated
    :param file: name of the file to be parsed
    """
    if os.path.isfile(file):
        result = []
        with open(file) as f:
            contents = f.read().split(delimiter)
            for each_line in contents:
                result.append(each_line)
        return result
    else:
        raise RuntimeError('word list ' + file + ' not found')

if __name__ == '__main__':
    generator = XkcdPasswordGenerator(parse('dictionary.csv'))
    print(generator.generate())
