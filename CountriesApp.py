import sys
import Validator
import FileIOHelper
from Country import Country

def main(args):
    name = ""
    population = 0
    action = 0
    # This creates a directory if there isn't one
    # FileIOHelper.createDir()
    # This creates a file if there isn't one
    # FileIOHelper.createOurFile()
    while not action == 3:
        print("\n\nWelcome to the Countries Maintenance Application!")
        print("1 - See the list of countries\n2 - Add a country\n3 - Exit\n")
        action = Validator.getInt("Enter a number: ", 1, 3)
        if action == 1:
            FileIOHelper.readFromFile()
        elif action == 2:
            country = Validator.getString("Enter country: ")
            population = Validator.getInteger("Enter population: ")
            new_country = Country(country, population)
            FileIOHelper.writeToFile(new_country)
        else:
            print("Buh-bye!")
            break



if __name__ == '__main__':
    sys.exit(main(sys.argv))