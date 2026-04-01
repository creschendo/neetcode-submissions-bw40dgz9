class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        top, bot = 0, m - 1

        while top <= bot:
            row = (bot + top) // 2

            if target < matrix[row][0]:
                bot = row - 1
            elif target > matrix[row][n - 1]:
                top = row + 1
            else:
                break
        
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[row][mid] < target:
                left = mid + 1
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                return True
        return False