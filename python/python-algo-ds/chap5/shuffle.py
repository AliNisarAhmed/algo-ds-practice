from random import randint

# C-5.14


def shuffle(arr):
    n = len(arr)

    for i in range(n):
        j = randint(i, n - 1)
        arr[j], arr[i] = arr[i], arr[j]

    return arr


print(shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
