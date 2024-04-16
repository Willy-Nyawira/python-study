"""
1. Check to see if user is logged in.
a. If logged in, ask if they would like to log out/quit.
i. Either quit or log out user and restart.
b. Else, ask if they would like to log in/register/quit.
i. If log in, ask user for e-mail/password.
1. If correct, log user in and restart.
2. Else, display error and restart.
ii. If register, ask for e-mail/password/password2.
1. If passwords match, save user and restart.
2. Else, display error and restart.
iii. If quit, say thank you and exit program.
"""
# import all necessary packages to be used
import csv
from IPython.display import clear_output
# handle user registration and writing to csv
def registerUser( ):
    with open("users.csv", mode="a", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        print("To register, please enter your info:")
        email = input("E-mail: ")
        password = input("Password: ")
        password2 = input("Re-type password: ")
        clear_output( )
        if password == password2:
            writer.writerow( [email, password] )
            print("You are now registered!")
        else:
            print("Something went wrong. Try again.")

# ask for user info and return true to login or false if incorrect info
def loginUser( ):
    print("To login, please enter your info:")
    email = input("E-mail: ")
    password = input("Password: ")
    clear_output( )
    with open("users.csv", mode="r") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            if row == [email, password]:
                print("You are now logged in!")
                return True
            print("Something went wrong, try again.")
            return False
         # variables for main loop
active = True
logged_in = False
 # main loop
while active:
    if logged_in:
        print("1. Logout\n2. Quit")
        choice = input("What would you like to do? ").lower()
        if choice == "logout":
            logged_in = False
            print("You are now logged out.")
        elif choice == "quit":
            active = False
            print("Thanks for using our software!")
    else:
        print("1. Login\n2. Register\n3. Quit")
        choice = input("What would you like to do? ").lower()
        clear_output()
        if choice == "register":
            registerUser()
        elif choice == "login":
            logged_in = loginUser()
        elif choice == "quit":
            active = False
            print("Thanks for using our software!")
        else:
            print("Sorry, please try again!")



