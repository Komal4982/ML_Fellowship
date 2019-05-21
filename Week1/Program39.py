from os import listdir
from os.path import isfile
from os.path import join


# get list of files from the given directory and skip directories
List_files = []
for f in listdir("/home/admin123/PycharmProjects/Machine Learing/Week1"):
    if isfile(join("/home/admin123/PycharmProjects/Machine Learing/Week1", f)):
        List_files.append(f)
        # gets each file from list end display on console
        for files in List_files:
            print(files)

