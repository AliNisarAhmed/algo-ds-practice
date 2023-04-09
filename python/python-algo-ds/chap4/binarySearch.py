# Recursive Binary search

def binary_search(data, target, low, high):
    if low > high:
        return False

    mid = (low + high) // 2
    if target == data[mid]:
        return True
    if target < data[mid]:
        return binary_search(data, target, low, mid - 1)

    return binary_search(data, target, mid + 1, high)
