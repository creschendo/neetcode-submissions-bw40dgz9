class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path  = set()

        # r = row
        # c = column
        # i = current letter
        def helper(r, c, i):
            # if we've reached the end of the word, 
            # return solution
            if i == len(word):
                return True
            
            # 1. Reached edge of board
            # 2. Current square isn't the right char
            # 3. Square already visited
            # --->  return False
            if (r < 0 or c < 0 or 
                r >= rows or c >= cols or
                word[i] != board[r][c] or
                (r,c) in path):
                return False
            
            # Square is valid, add to path
            path.add((r,c))

            # Recurse on each of the surrounding squares
            res = (helper(r + 1, c, i + 1) or
                   helper(r - 1, c, i + 1) or
                   helper(r, c - 1, i + 1) or 
                   helper(r, c + 1, i + 1))
            
            # Remove square so that it can be used by other paths
            path.remove((r,c))
            
            return res
        
        # Run recursion on each square in the board
        for r in range(rows):
            for c in range(cols):
                if helper(r, c, 0):
                    return True

        return False