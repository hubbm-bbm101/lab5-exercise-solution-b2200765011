'''
Guessing game! Pick a number randomly.
While user does not guess the number correctly give an instruction about the number and take another guess from user.
'''

import random
number = random.randint(1,100)
number_of_guesses = 0
guess = None
print("I picked a number between 1 and 100. Try to guess it!")

while True:
    guess= input("please pick a number or type 'quit': ")

    if guess =="quit":
        print("\nYou quit the game. If you want to play again please restart.")
        break
    else:
        guess = int(guess)


    if guess > number:
        print("decrease your number")
    elif guess < number:
        print("increase your number")
    else:
        print('''
        CORRECT!
        You made {} wrong guesses and game has ended.
        If you want to play again please restart.        
        '''.format(number_of_guesses))
        break
    number_of_guesses += 1
