class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def mark(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols
            or board[r][c] != "O"):
                return
            else:
                board[r][c] = "#"
                mark(r + 1, c)
                mark(r - 1, c)
                mark(r, c + 1)
                mark(r, c - 1)
                
        # left and right columns, including edge squares
        for i in range(rows):
            if board[i][0] == "O":
                mark(i, 0)
            if board[i][cols - 1] == "O":
                mark(i, cols - 1)

        # top and bottom rows, excluding edge squares
        for j in range(cols):
            if board[0][j] == "O":
                mark(0, j)
            if board[rows - 1][j] == "O":
                mark(rows - 1, j)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "#":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
        
    