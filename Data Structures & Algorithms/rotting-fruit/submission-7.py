class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        time = 0

        def addCell(r, c):
            if not (r in range(len(grid)) and c in range(len(grid[0])) 
            and grid[r][c] == 1):
                return 0
            else:
                grid[r][c] = 2
                q.append((r, c))
                return 1
        
        # count up initial fresh fruit, and add rotten to queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()

                fresh -= addCell(r + 1, c)
                fresh -= addCell(r - 1, c)
                fresh -= addCell(r, c + 1)
                fresh -= addCell(r, c - 1)
            time += 1
        
        return time  if fresh == 0 else -1