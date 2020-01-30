print('Imported module successfully...')

test = 'test_string'


def find_index(to_search, target):
    '''Find index of a value in a sequence'''
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1
