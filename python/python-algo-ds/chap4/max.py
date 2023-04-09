# R-4.1
def myMax(arr):
    """
        The running time and space usage are both O(n)
    """

    if len(arr) == 1:
        return arr[0]
    return max(arr[0], myMax(arr[1:]))


print(myMax([1, 2, 3, 4]))
