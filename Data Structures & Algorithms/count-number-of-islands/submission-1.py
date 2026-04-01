class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        sol = 0

        def helper(r, c):
            # bounds check
            if (r < 0 or c < 0 or
            r >= rows or c >= cols or
            grid[r][c] == "0"):
                return

            # set the square to a zero
            grid[r][c] = "0"

            # check the four directions
            # previous squares will be returned on since we set to zero
            helper(r - 1, c)
            helper(r + 1, c)
            helper(r, c - 1)
            helper(r, c + 1)

        # iterate over every square
        # every return from a one square is an additional island
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    helper(r, c)
                    sol += 1
        
        return sol