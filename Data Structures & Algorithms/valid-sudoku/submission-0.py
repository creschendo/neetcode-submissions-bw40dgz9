class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        
        for row in range(n):
            seen = set()
            for i in range(n):
                val  = board[row][i]
                if val == ".":
                    continue
                elif val in seen:
                    return False
                else:
                    seen.add(val)

        for col in range(n):
            seen = set()
            for i in range(n):
                val  = board[i][col]
                if val == ".":
                    continue
                elif val in seen:
                    return False
                else:
                    seen.add(val)

        for square in range(n):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i 
                    col = (square % 3) * 3 + j
                    val = board[row][col]
                    if val == ".":
                        continue
                    elif val in seen:
                        return False
                    else:
                        seen.add(val)
        return True