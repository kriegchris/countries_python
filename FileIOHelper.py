import os
import os.path

def readFromFile():
    pass

def writeToFile():
    pass

def createOurFile():
    pass

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