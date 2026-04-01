class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        rows, cols = len(matrix), len(matrix[0])

        # if n x n, just direct swap
        if rows == cols:
            for r in range(rows):
                for c in range(r):
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            print("pibble")
            return matrix

        # if n x m, make new matrix and just fill up
        sol = [[0] * rows for _ in range(cols)]

        for r in range(rows):
            for c in range(cols):
                sol[c][r] = matrix[r][c]
        
        return sol


        