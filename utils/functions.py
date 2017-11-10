from random_words import RandomWords


def random_words(number):
        rw = RandomWords()
        return [rw.random_word() for i in range(number)]
