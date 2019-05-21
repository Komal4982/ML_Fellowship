import os
import fnmatch


listOfFile = os.listdir('.')
pattern = "*.py"
for entry in listOfFile:

    if fnmatch.fnmatch(entry, pattern):
        print(entry)


