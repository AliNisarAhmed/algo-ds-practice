# Determine whether the largest element in the array is at least twice as much as every other number in the array.
# If it is, return the index of the largest element, or return -1 otherwise.

from typing import List


def dominantIndex(nums: List[int]) -> int:
    M = max(nums)
    max_index = 0

    for i, x in enumerate(nums):
        if not x == M and M < 2 * x:
            return -1
        if x == M:
            max_index = i

    return max_index


if __name__ == "__main__":
    a = [3, 6, 1, 0]
    print(dominantIndex(a))
    print(dominantIndex([1, 2, 3, 4]))
