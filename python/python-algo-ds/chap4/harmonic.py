# R-4.6
def harmonic(i):
    if i == 1:
        return 1
    return (1 / i) + harmonic(i - 1)


# R-4.7
def recursive_convert(str):
    k = len(str)
    if k == 1:
        return int(str)
    # incorrect
    return int(str[0]) * (10 ** (k - 1)) + recursive_convert(str[1:])


def recursive_convert2(str):
    k = len(str)
    if k == 1:
        return int(str)
    return int(str[-1]) + 10 * (recursive_convert2(str[:-1]))


print(recursive_convert2('1234'))


# C-4.9
def minmax(arr):
    k = len(arr)
    if k == 0:
        raise ValueError("Array cannot be empty")
    if k == 1:
        return (arr[0], arr[0])
    rest = arr[1:]
    (rmin, rmax) = minmax(rest)
    return (min(arr[0], rmin), max(arr[0], rmax))


print(minmax([1, 2, 3, 4, 5]))


# 4.10

def log_two(n):
    if n < 2:
        return 0
    return 1 + log_two(n // 2)


print('log_two: 16', log_two(16))


# C-4.11
def uniqueN2(arr, i=0):
    if i == len(arr) - 1:
        return True
    return (arr[i] not in arr[i + 1:]) and uniqueN2(arr, i + 1)


print(uniqueN2([1, 2, 3, 4]))
print(uniqueN2([1, 2, 3, 4, 1]))


# C-4.12
def product(m, n):
    if m == 0 or n == 0:
        return 0
    if m == 1:
        return n
    if n == 1:
        return m
    return m + product(m, n - 1)


print(product(4, 3))


# C-4.14
# https://www.cs.cmu.edu/~cburch/survey/recurse/hanoiex.html

def towerOfHanoi(disk, source=[], dest=[], spare=[]):
    if disk == 0:
        dest.append(source.pop())
    else:
        towerOfHanoi(disk - 1, source=source, dest=spare, spare=dest)
        dest.append(source.pop())
        towerOfHanoi(disk - 1, source=spare, dest=dest, spare=source)


source = [4, 3, 2, 1, 0]
dest = []
spare = []
print(source)
print(dest)
towerOfHanoi(4, source, dest, spare)
print(source)
print(dest)

# C-4.15


def print_subsets(arr):
    if arr == []:
        return [[]]

    else:
        rest_of_subsets = print_subsets(arr[1:])
        current_subsets = []
        for subset in rest_of_subsets:
            current = [arr[0]] + subset
            print(current)
            current_subsets.append(current)
        return rest_of_subsets + current_subsets


def subsets(arr):
    if arr == []:
        return [[]]
    else:
        # take subsets of all items except first one
        rest_of_subsets = subsets(arr[1:])

        # combine first item with all other subsets
        # and then combine them all and return
        return rest_of_subsets + [[arr[0]] + subset for subset in rest_of_subsets]


# print_subsets([1, 2, 3])
print(subsets([1, 2, 3]))
