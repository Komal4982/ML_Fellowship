
Str1 = 'w3resource'
print("Original string :", Str1)
my_str1 = {}
for letter in Str1:
    my_str1[letter] = my_str1.get(letter, 0) + 1
print("count of the from the string:", my_str1)





