from random import randrange
from map_base import MapBase


class HashMapBase(MapBase):
    """Abtract base class for map using hash-table with MAD compression"""

    def __init__(self, cap=11, p=109345121, load_factor=0.5):
        """Create an empty hash-table map"""
        self._table = cap * [None]  # bucket array
        self._n = 0  # number of entries in the map
        self._prime = p  # prime for MAD compression
        self._scale = 1 + randrange(p - 1)  # scale from 1 to p-1 for MAD
        self._shift = randrange(p)  # shift from 0 to p-1 for MAD
        self._load_factor = load_factor
        # Load factor: how much the underlying array is filled before resize is needed
        # defaults to 50%

    def _hash_function(self, k):
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)  # this call maintains self._n
        if self._n > int(
            len(self._table) * self._load_factor
        ):  # keep load factor <= given load factor
            self._resize(2 * len(self._table) - 1)

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n = 1

    def _resize(self, c):
        """Resize bucket array to capacity c"""
        old = list(self.items())  # use iteration to record existing items
        self._table = c * [None]  # then reset table to desired capacity
        self._n = 0  # n recomputed during subsequent adds
        for (k, v) in old:
            self[k] = v  # this call updates _n


# R-10.8 What would be a good hash code for a string of form
# "9X9XX99X9XX999999" where 9 is a digit and X is a letter
# Answer: cyclic shift or polynomial

# R-10.9
# h(i) = (3i + 5) mod 11 is the hash function
# draw the resulting map using separate chaining
# 12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5
# 12 = 8
# 44 = 5
# 13 = 0
# 88 = 5
# 23 = 8
# 94 = 1
# 11 = 5
# 39 = 1
# 20 = 10
# 16 = 9
# 5 = 9
# [[13], [94, 39], _, _, _, [44, 88, 11], _, _, [12, 23], [16, 5], [20]]

# R-10.10
# Same as above, but assume linear probing
# 00 01 02 03 04 05 06 07 08 09 10
# 13 94 39 16 05  44 88 11 12 23 20

# R-10.11
# Same as above, but assume quadratic probing
# [13, 94, 11, 20, _, 44, 88, 16, 12, 23, 39]
# 00 01 02 03 04 05 06 07 08 09 10
# 13 94 39 11    44 88 16 12 23 20 -> Error: no space found for 5


# R-10.13
# Worst case time for n entries in map with chaining? O(n^2), dump every entry into same bucket
# Best case: O(n)

# R-10.14
# [_, _, [54, 28, 41], _, _, [18], _, _, _, _, [10, 36], _, [25, 38, 12, 90]]
# Rehash above into table of size 19 using new hash function h(k) = 3k mod 17
# [_, _, 12, 18, 41, 30, 36, 25, _, 54, _, _, 38, 10, _, _, 28, _, _]


# --------------------------------------------------------------
# R-10.12
# Same as above but use double hashing
# h'(k) = 7 - (k mod 7)
# [13, 94, 23, 88, 39, 44, 11, 5, 12, 16, 20]

# Double Hasing:
# if A[h(k)] is already occupied
# then try A[h(k) + f(i) mod N] for i = 1, 2, 3...
# where f(i) = i * h'k

def hash1(n):
    return (3 * n + 5) % 11


def hash2(n):
    return 7 - (n % 7)


def double_hashing(arr):
    result = len(arr) * [None]

    for n in arr:
        hash_code = hash1(n)
        print("hash_code: " + repr(hash_code))
        if result[hash_code] is None:
            result[hash_code] = n
        else:
            for i in range(1, len(arr), 1):
                double_hash = (hash_code + i * hash2(n)) % len(arr)
                print(double_hash)
                if result[double_hash] is None:
                    result[double_hash] = n
                    break

    return result


# --------------------------------------------------------------

if __name__ == "__main__":
    print(double_hashing([12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5]))
