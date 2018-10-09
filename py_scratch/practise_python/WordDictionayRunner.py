#!/bin/env/python3

from py_scratch.practise_python.WordDictionary import OxfordOnlineWordDictionary

oxford_dictionary = OxfordOnlineWordDictionary()


def print_definitions(word):
    print(f'\n{word} :')
    print('\n'.join(oxford_dictionary.lookup(word)))


while True:
    word = input('\nWord to lookup (q to quit) : ').lower()
    if word == 'q':
        break
    print_definitions(word)
