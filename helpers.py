import random


def random_mail():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for _ in range(3):
        result += random.choice(letters)
    return result
