class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        seen = set()

        def trav(i, j):
            if (i < 0 or i >= len(grid) 
            or j < 0 or j >= len(grid[0])
            or grid[i][j] == 0):
                return 1
            if (i, j) in seen:
                return 0
            seen.add((i, j))

            perim = 0

            # down square
            perim += trav(i + 1, j)

            # up square
            perim += trav(i - 1, j)

            # right square
            perim += trav(i, j + 1)

            # left square
            perim += trav(i, j - 1)

            return perim

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return trav(i, j)
