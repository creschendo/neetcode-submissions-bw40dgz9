class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # reverse order of all rows
        r = 0
        while r < len(matrix) // 2:
            temp = matrix[r]
            matrix[r] = matrix[len(matrix) - 1 - r]
            matrix[len(matrix) - 1 - r] = temp
            r += 1
        
        # swap all top diagonal elements with their mirrored counterparts
        for i in range(len(matrix) - 1):
            for j in range(i + 1, len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        

        """
        [ 5,  1,  9, 11]
        [ 2,  4,  8, 10]
        [13,  3,  6,  7]
        [15, 14, 12, 16]

    
        [15, 14, 12, 16]
        [13,  3,  6,  7]
        [ 2,  4,  8, 10]
        [ 5,  1,  9, 11]


        [15, 13,  2,  5]
        [14,  3,  4,  1]
        [12,  6,  8,  9]
        [16,  7, 10, 11]
        """