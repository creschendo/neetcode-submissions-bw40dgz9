class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])

        self.sums = [[0] * (cols) for _ in range(rows)]
        pref = 0
        for i in range(cols):
            pref += matrix[0][i]
            self.sums[0][i] = pref

        
        for r in range(1, rows):
            pref = 0
            for c in range(cols):
                pref += matrix[r][c]
                self.sums[r][c] = pref + self.sums[r-1][c]



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        botright = self.sums[row2][col2]
        addback = 0
        print(botright)
        # subtract top
        if row1 > 0:
            print("subtop")
            botright -= self.sums[row1 - 1][col2]
            addback += 1

        # subtract left
        if col1 > 0:
            print("subleft")
            botright -= self.sums[row2][col1 - 1]
            addback += 1
        
        # add back double subtraction
        if addback == 2:
            botright += self.sums[row1 - 1][col1 - 1]

        return botright


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)