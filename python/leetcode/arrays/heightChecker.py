class Solution:

  # def heightChecker(self, heights):

  #   sorted = list(heights)

  #   sorted.sort()

  #   count = 0

  #   for i in range(len(heights)):

  #     if not sorted[i] == heights[i]:
  #       count += 1

  #   return count

  def heightChecker(self, heights):
    freq = [0] * 101

    for n in heights:
      freq[n] += 1

    count = 0
    hPtr = 1

    for h in heights:
      while freq[hPtr] == 0:
        hPtr += 1

      if not h == hPtr:
        count += 1

      freq[hPtr] -= 1

    return count


s = Solution()

s.heightChecker([1,1,4,2,1,3])