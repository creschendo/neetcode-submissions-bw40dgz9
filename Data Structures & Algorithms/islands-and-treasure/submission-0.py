class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        # given a cell, adds all neighbors to queue if they are 
        # in bounds, not walls, and not visited yet
        def addCell(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                (r, c) in visit or grid[r][c] == -1
            ):
                return
            visit.add((r, c))
            q.append([r, c])

        # initially add all treasure chests to queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        # iterate until queue is empty, initialize dist to 0
        dist = 0
        while q:
            for i in range(len(q)):
                # pop current cell, will initially just be setting treasure chests to 0
                r, c = q.popleft()

                # set cell to level distance, will always be shortest 
                grid[r][c] = dist

                # add each of 4 neighbors to queue
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)

            # increment distance at each level
            dist += 1