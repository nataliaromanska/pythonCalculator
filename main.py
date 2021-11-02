# pythonCalculator project
welcome = input("Enter your name:")
text = """
Lets do some numbers together!
Please provide the digits, and choose
the type of operation according to the info appearing on the screen
"""
print("Hello, " + welcome)
print(text)

digit1 = float(input("Enter your first digit:"))
digit2 = float(input("Enter your second digit:"))
operation = input("What do you want to do? (add/subtract/multiply/divide):")

if operation == "add":
    print(digit1, " + ", digit2, " = ", format((digit1 + digit2), '.3f'))
elif operation == "subtract":
    print(digit1, " - ", digit2, " = ", format((digit1 - digit2), '.3f'))
elif operation == "multiply":
    print(digit1, " * ", digit2, " = ", format((digit1 * digit2), '.3f'))
elif operation == "divide":
    print(digit1, " / ", digit2, " = ", format((digit1 / digit2), '.3f'))
else:
    print("Oops, something went wrong! Check your input and start once again.")

middle_check = input("Do you want to count more? (yes/no):")

if input == "yes":
    print("Ok, let's do it!")