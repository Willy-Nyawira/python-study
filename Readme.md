Hangman Game
Description
This Python script implements a simple command-line version of the classic game Hangman. The player guesses letters to uncover a hidden word. They have limited attempts before the game ends.

Usage
Run the hangman.py script.
Follow the prompts to guess letters or quit the game.
Files
hangman.py: Contains the main Hangman game implementation.
Dependencies
random.choice: Used to randomly select a word from a predefined list.
IPython.display.clear_output: Utilized for clearing the output in the IPython environment.
Code and Explanation
python
Copy code
# import additional functions
from random import choice
from IPython.display import clear_output

# declare game variables
words = ["tree", "basket", "chair", "paper", "python"]
word = choice(words) # randomly chooses a word from words list
guessed, lives, game_over = [], 7, False # multi-variable assignment

# create main game loop
while not game_over:
    ans = input("Type quit or guess a letter: ").lower()
    if ans == "quit":
        print("Thanks for playing.")
        game_over = True
The script starts by importing necessary functions and declaring game variables. It then enters a main game loop where the player guesses letters until they either quit or the game ends.

Receipt Generator
Description
This Python script generates a receipt for a fictional shopping transaction. It includes details such as product names, prices, company information, and a total.

Usage
Run the receipt.py script.
The receipt will be displayed in the console.
Files
receipt.py: Contains the receipt generation logic.
How to Use
Run the script.
The receipt containing product details, company information, and total will be printed.
Code and Explanation
python
Copy code
# create a product and price for three items
p1_name, p1_price = "Books", 49.95
p2_name, p2_price = "Computer", 579.99
p3_name, p3_price = "Monitor", 124.89

# create a company name and information
company_name = "coding temple, inc."
company_address = "283 Franklin St."
company_city = "Boston, MA"

# declare ending message
message = "Thanks for shopping with us today!"

# create a top border
print("*" * 50)

# print company information first, using format
print("\t\t{}".format(company_name.title()))
print("\t\t{}".format(company_address))
print("\t\t{}".format(company_city))

# print a line between sections
print("=" * 50)

# print out header for section of items
print("\tProduct Name\tProduct Price")

# create a print statement for each product
print("\t{}\t\t${}".format(p1_name.title(), p1_price))
print("\t{}\t${}".format(p2_name.title(), p2_price))
print("\t{}\t\t${}".format(p3_name.title(), p3_price))

# print a line between sections
print('=' * 50)

# calculate total price and print out
total = p1_price + p2_price + p3_price
print("\t\tTotal=${}".format(total))

# print a line between sections
print("=" * 50)

# output thank you message
print("\n\t{}\n".format(message))

# create a bottom border
print("*" * 50)
The script generates a receipt with product details, company information, and a total price.

Shopping Cart
Description
This Python script simulates a simple shopping cart system. Users can add, remove, view, or clear items in their cart.

Usage
Run the shoppingcart.py script.
Follow the prompts to interact with the shopping cart.
Files
shoppingcart.py: Contains the shopping cart implementation.
Dependencies
IPython.display.clear_output: Used for clearing the output in the IPython environment.
Code and Explanation
python
Copy code
# import necessary functions
from IPython.display import clear_output

# global list variable
cart = []

# create function to add items to cart
def addItem(item):
    clear_output()
    cart.append(item)
    print("{} has been added.".format(item))

# create function to remove items from cart
def removeItem(item):
    clear_output()
    try:
        cart.remove(item)
        print("{} has been removed.".format(item))
    except:
        print("Sorry we could not remove that item.")

# create a function to show items in cart
def showCart():
    clear_output()
    if cart:
        print("Here is your cart:")
        for item in cart:
            print("- {}".format(item))
    else:
        print("Your cart is empty.")

# create function to clear items from cart
def clearCart():
    clear_output()
    cart.clear()
    print("Your cart is empty.")

# create main function that loops until the user quits
def main():
    done = False
    while not done:
        ans = input("What would you like to do? (add/remove/show/clear/quit): ").lower()
        if ans == "add":
            item = input("What would you like to add? ").title()
            addItem(item)
        elif ans == "remove":
            showCart()
            item = input("What item would you like to remove? ").title()
            removeItem(item)
        elif ans == "show":
            showCart()
        elif ans == "clear":
            clearCart()
        elif ans == "quit":
            print("Thanks for using our program.")
            showCart()
            done = True
        else:
            print("Sorry, that was not an option.")

# Run the program
main()
The script defines functions for adding, removing, displaying, and clearing items in the shopping cart. It then runs a main loop to interact with the user.

Calculator
Description
This Python script implements a basic calculator. It performs addition, subtraction, multiplication, or division based on user input.

Usage
Run the calculator.py script.
Follow the prompts to select an operation and input numbers.
Files
calculator.py: Contains the calculator implementation.
How to Use
Start the script.
Choose the desired operation (addition, subtraction, multiplication, or division).
Input the numbers to perform the operation.
The result will be displayed.
Code and Explanation
python
Copy code
# step 1: ask user for calculation to be performed
operation = input("Would you like to add/subtract/multiply/divide? ").lower()
print("You chose {}.".format(operation)) # for testing purposes

# step 2: ask for numbers, alert order matters for subtracting and dividing
if operation == "subtract" or operation == "divide":
    print("You chose {}.".format(operation))
    print("Please keep in mind that the order of your numbers matter.")
num1 = input("What is the first number? ")
num2 = input("What is the second number? ")
print("First Number: {}".format(num1)) # for testing purposes
print("Second Number