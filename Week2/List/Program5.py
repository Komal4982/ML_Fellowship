

def sort_list_last(tuples):
    return sorted(tuples, key=last)


def last(n): return n[-1]


print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

