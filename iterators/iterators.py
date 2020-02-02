'''[sentence, a function generator]

Returns:
    [type] -- [description]

Yields:
    [string] -- [next word in a sentence]
'''


def sentence(my_sentence):
    for word in my_sentence.split():
        yield word


my_sentence = sentence('This is a test')

for word in my_sentence:
    print(word)


'''[Sentence, a class generator]

Raises:
    StopIteration: [When the list of words is exhausted]

Returns:
    [iterator] -- [A generator that returns a word in a sentence on each iteration in order]
'''


class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence.split()
        self.index = 0

    def __iter__(self):
        '''Must return self, because self has the __next__() method'''
        return self

    def __next__(self):
        '''Must be present, it runs on calling (next('This classes object'))'''
        if self.index >= len(self.sentence):
            raise StopIteration
        current = self.sentence[self.index]
        self.index += 1
        return current


sent = Sentence('This is a test')

for word in sent:
    print(word)
