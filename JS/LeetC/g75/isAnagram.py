class Solution:

    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        obj = dict()

        for c in s:
            obj[c] = obj.get(c, 0) + 1

        for c in t:
            if not obj.get(c):
                return False
            else:
                obj[c] -= 1

        return True
