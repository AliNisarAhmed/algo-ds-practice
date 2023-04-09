from typing import List

def pivotIndex(nums: List[int]) -> int:
    S = sum(nums)
    leftSum = 0

    for i, x in enumerate(nums):
        if leftSum == (S - leftSum -  x):
            return i
        leftSum += x
    return -1


if __name__ == "__main__":
    a = [1, 7, 3, 6, 5, 6]
    r = pivotIndex(a)
    print(r)
