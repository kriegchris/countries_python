import sys
import Validator
import FileIOHelper

def main(args):
    name = ""
    population = 0
    action = 0
    # FileIOHelper.createDir()
    while not action == 3:
        print("\nWelcome to the Countries Maintenance Application!")
        print("1 - See the list of countries\n2 - Add a country\n3 - Exit\n")
        action = Validator.getInt("Enter a number: ", 1, 3)
        if action == 1:
            pass
        elif action == 2:
            pass
        else:
            break
        print("Buh-bye!")


if __name__ == '__main__':
    sys.exit(main(sys.argv))