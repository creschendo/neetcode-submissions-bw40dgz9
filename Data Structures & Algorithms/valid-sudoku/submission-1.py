class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        for row in range(n):
            seen = set()
            for i in range(n):
                val = board[row][i]
                if val in seen:
                    return False
                elif val == ".":
                    continue
                else:
                    seen.add(val)

        for col in range(n):
            seen = set()
            for i in range(n):
                val = board[i][col]
                if val in seen:
                    return False
                elif val == ".":
                    continue
                else:
                    seen.add(val)
        
        for square in range(n):
            seen = set()
            
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    elif board[row][col] in seen:
                        return False
                    else:
                        seen.add(board[row][col])
        return True