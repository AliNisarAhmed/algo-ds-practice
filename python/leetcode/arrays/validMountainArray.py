class Solution:

    def validMountainArray(self, arr):

        i = 0
        l = len(arr)

        while i < l - 1 and arr[i] < arr[i + 1]:
            i += 1

        if i == 0 or i >= l - 1:
            return False

        while i < l - 1 and arr[i] > arr[i + 1]:
            i += 1

        return i == l - 1


s = Solution()

arr = [2, 1]

print(s.validMountainArray(arr))
