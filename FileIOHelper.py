import os
import os.path
from os import path
from Country import Country

def readFromFile():
    fileName = "countries/countries.txt"
    with open(fileName, "r") as myFile:
        for line in myFile.readlines():
            lines = line.split(",")
            country = Country(lines[0], lines[1])
            print('{} (pop {:,d})'.format(country.name, int(country.population)))


def writeToFile(country):
    fileName = "countries/countries.txt"
    with open(fileName, "a") as myFile:
        myFile.write("\n"+ str(country))

def createOurFile():
    fileName = "countries/countries.txt"
    if not path.exists(fileName):
        try:
            with open(fileName, "r") as myFile:
                print("The file was created successfully!")
        except IOError:
            print("Something went terribly wrong!")
    else:
        print("The file already exists!")

def createDir():
    path = "countries"
    if not os.path.isdir(path):
        try:
            os.mkdir(path)
        except OSError:
            print("Creation of the directory %s failed" % path)
        else:
            print("Successfully created the directory %s " % path)
    else:
        print("The folder already exists!")