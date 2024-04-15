from random import randint
from IPython.display import clear_output
guessed = False
number = randint(0, 100)
guesses = 0
while not guessed:
    ans = input("Try to guess the number I am thinking of!")   

    guesses += 1
    clear_output( )
    if int(ans) == number:
        print("Congrats! You guessed it correctly.")
        print( "It took you { } guesses!".format(guesses) )
        break
    elif int(ans) > number:
        print("The number is lower than what you guessed.")
        break
    elif int(ans) < number:
        print("The number is greater than what you guessed.")
        