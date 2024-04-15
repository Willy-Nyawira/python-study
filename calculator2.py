# Step 1: ask user for calculation to be performed
operation = input("Would you like to add/subtract/multiply/divide? ").lower()
print("You chose {}.".format(operation))  # for testing purposes

# Step 2: ask for numbers, alert order matters for subtracting and dividing
if operation == "subtract" or operation == "divide":
    print("You chose {}.".format(operation))
    print("Please keep in mind that the order of your numbers matter.")
num1 = input("What is the first number? ")
num2 = input("What is the second number? ")
print("First Number: {}".format(num1))  # for testing purposes
print("Second Number: {}".format(num2))  # for testing purposes

try:
    # Step 3: setup try/except for mathematical operation
    # Step 3a: immediately try to convert numbers input to floats
    num1, num2 = float(num1), float(num2)
    # Step 3b: perform operation and print result
    if operation == "add":
        result = num1 + num2
        print("{} + {} = {}".format(num1, num2, result))
    elif operation == "subtract":
        result = num1 - num2
        print("{} - {} = {}".format(num1, num2, result))
    elif operation == "multiply":
        result = num1 * num2
        print("{} * {} = {}".format(num1, num2, result))
    elif operation == "divide":
        result = num1 / num2
        print("{} / {} = {}".format(num1, num2, result))
    else:
        # else will be hit if they didn't chose an option correctly
        print("Sorry, but '{}' is not an option.".format(operation))
except:
    print("Error: Improper numbers used. Please try again.")
