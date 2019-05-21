import os.path
import time


print("Last modified: %s" % time.ctime(os.path.getmtime("abc.txt")))
print("accessed: %s" % time.ctime(os.path.getatime("abc.txt")))
print("Created: %s" % time.ctime(os.path.getctime("abc.txt")))


print(time.ctime(os.path.getmtime("abc.txt")))
print(time.time())
