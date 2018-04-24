"""Correct the syntax in this file.

This file doesn't run yet.
Go through it and change it until it runs.
"""
import string

def getLetter(index):
    string = "oli is a screw"
    
    return string[index-2:index]

print(getLetter(0))


def week2exersise2(secret_word):
    indices = [12, 2, 26, 7, 0, 12, 12, 4, 17]
    wordArray = []  # hint: should this be a dictionary?
    for index in indices:
        wordArray.append[getLetter(index)]

    wordArray[0] = wordArray[0].upper()
    wordArray[1] = wordArray[1].upper()
    wordArray[3] = wordArray[3].upper()
    secret_word = a.join(wordArray)
    return secret_word

print(week2exersise2(0))


if __name__ = = __main__:
    print (week2exersise2())
