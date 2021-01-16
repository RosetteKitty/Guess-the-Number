import random

number = (random.randrange(10, 50))
guess = int(input('Guess the number between 10 and 50: '))

while guess != number:
    if guess < number:
        print('You need to guess higher')
        guess = int(input('Guess the number between 10 and 50: '))
    else:
        print('You need to guess lower')
        guess = int(input('Guess the number between 10 and 50: '))

print('You guessed!')
