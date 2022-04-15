from typing import List
from math import log10, floor


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(len(str(i)) % 2 == 0 for i in nums)

    def findNumbers2(self, nums: List[int]) -> int:
        count = 0
        for n in nums:
            digits = floor(log10(n)) + 1 # formula to calculate number of digits in a decimal number
            if digits % 2 == 0:
                count += 1
        return count

s = Solution()
s.findNumbers([100000])
