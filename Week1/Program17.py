import time


def display_time(n):
    start_time = time.time()
    add = 0
    for i in range(1, n):
        add += i
    print(add)
    end_time = time.time()
    return end_time - start_time


n = 50
execute_time = display_time(n)
print(execute_time)












