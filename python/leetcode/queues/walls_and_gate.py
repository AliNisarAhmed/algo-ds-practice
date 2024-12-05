"""
-1  = a wall or an obstacle
0   = a gate
INF = empty room

example:
    [
            [2147483647,-1,0,2147483647],
            [2147483647,2147483647,2147483647,-1],
            [2147483647,-1,2147483647,-1],
            [0,-1,2147483647,2147483647]
    ]
"""
from typing import List
from collections import deque


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """modify rooms in place"""
        queue = deque([])

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:  # its a gate
                    queue.append([i, j])

        while queue:
            i, j = queue.popleft()

            for r, c in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= r < len(rooms) and 0 <= c < len(rooms[0]) \
                        and rooms[r][c] == 2147483647:
                    rooms[r][c] = rooms[i][j] + 1
                    queue.append([r, c])


if __name__ == "__main__":
    s = Solution()
    l = [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647]
    ]
    s.wallsAndGates(l
                    )
    print(l)
