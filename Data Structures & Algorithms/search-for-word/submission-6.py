class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        seen = set()
        def bt(row, col, curr):
            if (row < 0 or row >= m or
            col < 0 or col >= n or 
            (row, col) in seen or
            board[row][col] != word[curr]):
                return False

            if curr == len(word) - 1:
                return True
            
            seen.add((row, col))
            dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for x, y in dirs:
                call = bt(row + x, col + y, curr + 1)
                if call:
                    return True

            seen.remove((row, col))

            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:

                    if bt(i, j, 0):
                        return True
        
        return False
        

