class Solution:
  def removeDuplicates(self, nums):
    i = j = 0

    while j < len(nums):

      while nums[i] == nums[j]:
        j += 1

      nums[i] = nums[j]

      i += 1

    return i