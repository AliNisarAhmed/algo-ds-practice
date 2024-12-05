from typing import List
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque()
        queue.append(['0000', 0])
        seen = set(deadends)

        while queue:
            node, depth = queue.popleft()
            if node == target:
                return depth

            if node in seen:
                continue

            seen.add(node)
            for nei in self.neighbors(node):
                queue.append([nei, depth + 1])

        return -1

    def neighbors(self, node):
        for i in range(4):
            x = int(node[i])
            for d in [-1, 1]:
                y = (x + d) % 10
                yield node[:i] + str(y) + node[i+1:]


if __name__ == "__main__":
    s = Solution()
    print(s.openLock(['8888'], '0009'))
    print(s.openLock(["0201", "0101", "0102", "1212", "2002"], "0202"))
