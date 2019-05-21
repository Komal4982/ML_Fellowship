import os
print("\nEffective group id: ", os.getegid())
print("Effective user id: ", os.geteuid())
print("Real group id: ", os.getgid())
print("List of supplemental group ids with the current process: ", os.getgroups())
print()
