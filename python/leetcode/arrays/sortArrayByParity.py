class Solution:

  def sortArrayByParity(self, nums):

    odd_pos = 0

    for i in range(len(arr)):
      if nums[i] % 2 == 0:
        nums[odd_pos], nums[i] = nums[i], nums[odd_pos]
        odd_pos += 1

    return nums

