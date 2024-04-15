# import additional functions
from random import choice
from IPython.display import clear_output
# declare game variables
words = [ "tree", "basket", "chair", "paper", "python" ]
word = choice(words) # randomly chooses a word from words list
guessed, lives, game_over = [ ], 7, False # multi variable assignment
# create a list of underscores to the length of the word
[ "_ " ] * len(word)
# create main game loop
while not game_over:
    ans = input("Type quit or guess a letter: ").lower( )
    if ans == "quit":
        print("Thanks for playing.")
        game_over = True
        while not game_over:
            # output game information
            hidden_word = "".join(guessed)
            print( "Word to guess: { }".format(hidden_word) )
            print( "Lives: {}".format(lives) )
            ans =input("Type quit or guess a letter: ").lower()  # Prompt for user input