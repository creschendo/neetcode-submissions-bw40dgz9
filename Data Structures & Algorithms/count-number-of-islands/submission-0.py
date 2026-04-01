class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        copy = grid.copy()
        rows, cols = len(grid), len(grid[0])

        sol = 0

        def helper(r, c):
            # bounds check
            if (r < 0 or c < 0 or
            r >= rows or c >= cols or
            grid[r][c] == "0"):
                return

            grid[r][c] = "0"

            helper(r - 1, c)
            helper(r + 1, c)
            helper(r, c - 1)
            helper(r, c + 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    helper(r, c)
                    sol += 1
        
        return sol