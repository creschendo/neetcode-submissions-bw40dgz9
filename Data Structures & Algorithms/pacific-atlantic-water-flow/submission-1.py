class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        # Reverse flow simulation
        # - starting from each ocean edge, do a dfs until no squares 
        #   can be reached, going only if the next square is higher 
        #   than the current. All visited squares are part of the solution
        def helper(r, c, visit, prev):
            # if out of bounds, or already visited, or lower than before, return
            if ((r, c) in visit or
            r < 0 or c < 0 or
            r == rows or c == cols or 
            heights[r][c] < prev):
                return

            # valid square, add 
            visit.add((r,c))

            # check all four directions, updating new height
            helper(r + 1, c, visit, heights[r][c])
            helper(r - 1, c, visit, heights[r][c])
            helper(r, c + 1, visit, heights[r][c])
            helper(r, c - 1, visit, heights[r][c])

        # check top and bottom row
        for c in range(cols):
            # the top row, which borders the pacific
            helper(0, c, pac, heights[0][c])

            # the bottom row, which borders the atlantic
            helper(rows - 1, c, atl, heights[rows - 1][c])
        
        # check the left and right columns
        for r in range(rows):
            # the left column, which borders the pacific
            helper(r, 0, pac, heights[r][0])

            # the right column, which borders the atlantic
            helper(r, cols - 1, atl, heights[r][cols-1])
        
        # calculate the union and return
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append((r, c))
        
        return res
