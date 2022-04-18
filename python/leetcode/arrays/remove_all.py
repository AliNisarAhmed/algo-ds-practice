class Solution:
  def removeElement(self, nums, val):

    i = 0
    for j in range(len(nums)):
      if (nums[j] != val):
        nums[i] = nums[j]
        i += 1

    return i

s = Solution()
arr = [3, 2, 2, 3]
s.removeElement(arr, 3)
print(arr)