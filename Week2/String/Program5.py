
def find_longest_word(words):
    word_len = []
    for n in words:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]


print(find_longest_word(["PHP", "Exercises", "Backend"]))






