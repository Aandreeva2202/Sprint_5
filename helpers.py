import random

def random_mail():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for _ in range(5):
        result += random.choice(letters)
    return result

mail = random_mail()
print(mail)