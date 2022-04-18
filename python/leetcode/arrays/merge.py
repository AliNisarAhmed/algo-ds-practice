class Solution:
  def merge(self, nums1, m, nums2, n):
    if n == 0:
      return
    if m == 0:
      for i in range(n):
        nums1[i] = nums2[i]
      return

    left = m - 1
    right = n - 1

    for j in range(m + n - 1, -1, -1):

      if right < 0:
        break

      if left < 0 or nums2[right] >= nums1[left]:
        nums1[j] = nums2[right]
        right -= 1
      else:
        nums1[j] = nums1[left]
        left -= 1


s = Solution()
arr = [1, 2, 3, 0, 0, 0]
s.merge(arr, 3, [2, 5, 6], 3)
print(arr)