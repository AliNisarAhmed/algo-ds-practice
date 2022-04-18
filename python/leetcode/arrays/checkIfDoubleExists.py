class Solution:

    def checkIfExist(self, arr):
        dict = {}

        for item in arr:
            if dict.get(2 * item) or (item % 2 == 0 and dict.get(item // 2)):
                return True
            else:
                dict[item] = True

        return False


s = Solution()

arr = [10, 2, 5, 3]

print(s.checkIfExist(arr))
