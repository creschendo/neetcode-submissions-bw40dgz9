class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        m, n = len(grid), len(grid[0])
        maxSize = 0
        def traverse(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return 0
            elif grid[r][c] == 0 or (r, c) in visited:
                return 0
            visited.add((r, c))

            up = traverse(r - 1, c)
            down = traverse(r + 1, c)
            left = traverse(r, c - 1)
            right = traverse(r, c + 1)

            return 1 + up + down + left + right

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = traverse(i, j)
                    maxSize = max(maxSize, area)

        return maxSize