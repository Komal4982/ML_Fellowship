def max_min(data):
    l = data[0]
    s = data[0]

    for num in data:
        if num > l:
          l = num
        elif num < s:
            s = num
    return l, s



print(max_min(['85', '45', '90', '75', '64', '84', '95', '1', '50']))



