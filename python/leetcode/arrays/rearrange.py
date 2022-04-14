def rearrange(arr, k, index=0):
    l = len(arr)
    if index >= l:
        return []
    else:
        if arr[index] > k:
            return rearrange(arr, k, index + 1) + [arr[index]]
        else:
            return [arr[index]] + rearrange(arr, k, index + 1)


def rearrange2(arr, k):
    return rearrange_rec(arr, k, 0, len(arr) - 1)


def rearrange_rec(arr, k, start, stop):
    if start >= stop:
        return arr
    else:
        if arr[start] > k:
            arr[start], arr[stop] = arr[stop], arr[start]
            return rearrange_rec(arr, k, start, stop - 1)
        elif arr[stop] < k:
            arr[start], arr[stop] = arr[stop], arr[start]
            return rearrange_rec(arr, k, start + 1, stop)
        else:
            return rearrange_rec(arr, k,  start + 1,  stop - 1)


print(rearrange2([10, 14, 15, 48, 85, 38, 109, 98, 90, 5], 80))
