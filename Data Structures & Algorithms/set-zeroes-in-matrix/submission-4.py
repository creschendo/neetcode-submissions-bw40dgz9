class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        # Use the matrix itself as flags for zeroed rows and columns
        #   - The top row will store whether the column contains a zero, denoted by 0
        #   - The left column will store whether the row contains a zero, denoted by 0
        #   - The top boolean will store whether the top row contains a zero
        #   - The top left square (matrix[0][0]) will store whether the left column contains a zero
        top = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i == 0:
                        top = True
                    else:
                        matrix[i][0] = 0
            

        # set general squares
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # set left column
        if matrix[0][0] == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        
        # set top row
        if top:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        
