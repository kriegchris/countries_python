import re

# get any valid integer
def getInt(prompt):
    number = input(prompt)
    while not number.isdigit():
        print("Sorry, I can't read that. Enter a whole number, using digits.")
        number = input(prompt)
    number = int(number)
    return number

# get any valid integer within a range
def getInt(prompt, minimum, maximum):
    number = input(prompt)
    while not number.isdigit():
        print("Sorry, I can't read that. Enter a whole number, using digits.")
        number = input(prompt)
    number = int(number)
    while number < minimum:
        print("The number must be at least " + str(minimum))
        number = input(prompt)
        number = int(number)
    while number > maximum:
        print("the number must be no greater than " + str(maximum))
        number = input(prompt)
        number = int(number)
    return number
# get any valid double
def getDouble(prompt):
    decimal = input(prompt)
    while not decimal.isdecimal():
        print("Sorry, I can't read that. Enter a decimal, using digits.")
        decimal = input(prompt)
    decimal = float(decimal)
    return decimal

# get any valid double within a range
def getDouble(prompt, minimum, maximum):
    decimal = input(prompt)
    while not decimal.isdecimal():
        print("Sorry, I can't read that. Enter a decimal, using digits.")
        decimal = input(prompt)
    while decimal < minimum:
        print("The number must be at least " + str(minimum))
        decimal = input(prompt)
        decimal = int(decimal)
    while decimal > maximum:
        print("the number must be no greater than " + str(maximum))
        decimal = input(prompt)
        decimal = int(decimal)
    return decimal

# get any valid string
def getString(prompt):
    return input(prompt)

# get a string of input from the user that must match the given regex
def getStringMatchingRegex(prompt, regex):
    input = getString(prompt)
    while not re.match(regex, input):
        print("Input must match the appropriate format")
        input = getString(prompt)
    return input



            
            
