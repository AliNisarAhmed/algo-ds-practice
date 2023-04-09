def reverse(arr, start, stop):
    if start < stop - 1:
        arr[start], arr[stop - 1] = arr[stop - 1], arr[start]
        reverse(arr, start + 1, stop - 1)


arr = [1, 2, 3]
reverse(arr, 0, 3)
print(arr)


# C-4.17
def is_palindrome(str):
    if len(str) <= 1:
        return True

    return str[0] == str[-1] and is_palindrome(str[1:-1])


print('is_palindrome', is_palindrome(''))
print('is_palindrome', is_palindrome('r'))
print('is_palindrome', is_palindrome('racecar'))
print('is_palindrome', is_palindrome('gohangasalamiimalasagnahog'))
print('is_palindrome', is_palindrome('notapalindrome'))

# C-4.18


def more_vowels_or_consonants(str):
    def count_vowels_and_consonants(str, v=0, c=0):
        if len(str) == 0:
            return (v, c)
        elif str[0] in 'aeiou':
            return count_vowels_and_consonants(str[1:], v+1, c)
        else:
            return count_vowels_and_consonants(str[1:], v, c+1)

    (vowels, consonants) = count_vowels_and_consonants(str)
    return vowels > consonants


print(more_vowels_or_consonants('aaaabb'))
print(more_vowels_or_consonants('abbbbbb'))

# C-4.19


def _sort_evens_odds(data, low, high):
    if low < high:
        if data[high] % 2 == 0:
            data[low], data[high] = data[high], data[low]
            return _sort_evens_odds(data, low + 1, high)
        else:
            # data[high] is odd and already at the end of the array
            return _sort_evens_odds(data, low, high - 1)


def sort_evens_odds(data):
    _sort_evens_odds(data, 0, len(data) - 1)
    return data


print(sort_evens_odds([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# C-4.20

def _sort_by_k(S, k, low, high):
    if low < high:
        if S[high] <= k:
            S[low], S[high] = S[high], S[low]
            return _sort_by_k(S, k, low + 1, high)
        else:
            return _sort_by_k(S, k, low, high - 1)


def sort_by_k(S, k):
    _sort_by_k(S, k, 0, len(S) - 1)
    return S


print(sort_by_k([7, 3, 9, 8, 1, 2], 5))


# C-4.21

def _two_sum_recursive(data, k, low, high):
    if low < high:
        if data[low] + data[high] == k:
            return (low, high)
        elif data[low] + data[high] > k:
            return _two_sum_recursive(data, k, low, high - 1)
        else:
            return _two_sum_recursive(data, k, low + 1, high)
    return -1


def two_sum_recursive(data, k):
    return _two_sum_recursive(data, k, 0, len(data) - 1)


print(two_sum_recursive([1, 2, 3, 4, 5, 6, 7], 13))
print(two_sum_recursive([1, 2, 3, 4, 5, 6, 7], 14))
