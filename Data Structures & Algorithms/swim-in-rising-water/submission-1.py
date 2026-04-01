class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        # min cost path, djikstras
        N = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visit.add((0, 0))
        while minH:
            # pop tuple with current max height t, row r, and column c
            t, r, c = heapq.heappop(minH)

            # return t if we've reached the bottom right
            if r == N - 1 and c == N - 1:
                return t

            # add each valid neighbor
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if (neiR < 0 or neiC < 0 or
                neiR == N or neiC == N or
                (neiR, neiC) in visit):
                    continue

                # mark neighbor as visited
                visit.add((neiR, neiC))

                # push the max of current max height and new square
                # height, and row and column
                heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])