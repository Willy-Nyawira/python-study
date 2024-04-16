import csv
import random
import string
from IPython.display import clear_output

# Function to register a new user
def registerUser():
    with open("users.csv", mode="a", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        print("To register, please enter your info:")
        email = input("E-mail: ")
        password = input("Password: ")
        password2 = input("Re-type password: ")
        clear_output()
        if password == password2:
            writer.writerow([email, password])
            print("You are now registered!")
        else:
            print("Passwords do not match. Please try again.")

# Function to log in a user
def loginUser():
    print("To login, please enter your info:")
    email = input("E-mail: ")
    password = input("Password: ")
    clear_output()
    with open("users.csv", mode="r") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            if row == [email, password]:
                print("You are now logged in!")
                return email  # Return the email of the logged-in user
        print("Incorrect email or password.")
        return None

# Function to generate a temporary password
def generateTempPassword():
    temp_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return temp_password

# Function to send the temporary password to the user's email address
def sendTempPassword(email, temp_password):
    # Add code here to send the temporary password to the user's email address
    print(f"A temporary password has been sent to {email}. Please check your email.")

# Function to handle the "forgot password" functionality
def forgotPassword():
    email = input("Enter your email address: ")
    # Check if the email exists in the CSV file
    with open("users.csv", mode="r") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            if row[0] == email:
                # Generate a temporary password
                temp_password = generateTempPassword()
                # Update the user's password in the CSV file with the temporary password
                with open("users.csv", mode="r") as f:
                    reader = csv.DictReader(f, delimiter=",")
                    with open("users.csv", mode="w", newline="") as f:
                        fieldnames = ["email", "password"]
                        writer = csv.DictWriter(f, fieldnames=fieldnames)
                        writer.writeheader()
                        for row in reader:
                            if row["email"] == email:
                                row["password"] = temp_password
                            writer.writerow(row)
                # Send the temporary password to the user's email address
                sendTempPassword(email, temp_password)
                return
        print("Email address not found.")

# Function to change user password
def changePassword(email):
    newPassword = input("Enter your new password: ")
    newPassword2 = input("Re-type your new password: ")
    if newPassword == newPassword2:
        # Open the CSV file in read mode and create a list of dictionaries
        with open("users.csv", mode="r") as f:
            reader = csv.DictReader(f, delimiter=",")
            # Open the CSV file in write mode and write the updated information
            with open("users.csv", mode="w", newline="") as f:
                fieldnames = ["email", "password"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    if row["email"] == email:
                        row["password"] = newPassword
                    writer.writerow(row)
        print("Password updated successfully!")
    else:
        print("Passwords do not match. Please try again.")

# Main loop
active = True
logged_in_email = None

while active:
    if logged_in_email:
        print("1. Change Password\n2. Logout\n3. Quit")
        choice = input("What would you like to do? ").lower()
        if choice == "change password":
            changePassword(logged_in_email)
        elif choice == "logout":
            logged_in_email = None
            print("You are now logged out.")
        elif choice == "quit":
            active = False
            print("Thanks for using our software!")
        else:
            print("Invalid choice. Please try again.")
    else:
        print("1. Login\n2. Register\n3. Forgot Password\n4. Quit")
        choice = input("What would you like to do? ").lower()
        clear_output()
        if choice == "register":
            registerUser()
        elif choice == "login":
            logged_in_email = loginUser()
        elif choice == "forgot password":
            forgotPassword()
        elif choice == "quit":
            active = False
            print("Thanks for using our software!")
        else:
            print("Invalid choice. Please try again!")
