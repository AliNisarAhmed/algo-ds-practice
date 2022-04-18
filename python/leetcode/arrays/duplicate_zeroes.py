from typing import List

class Solution:

  def duplicateZeros(self, arr):
    count_zeroes = z = arr.count(0)

    arr.extend([0] * count_zeroes)

    for i in range(len(arr) - 1 - count_zeroes, -1, -1):
      arr[i + count_zeroes] = arr[i]
      if arr[i] == 0:
        count_zeroes -= 1
        arr[i + count_zeroes] = arr[i]
    if z > 0:
      del arr[-1 * z:]

s = Solution()
arr = [1, 0, 2, 3, 0, 4, 5, 0]
arr = [1, 2, 3]
s.duplicateZeros(arr)
print(arr)