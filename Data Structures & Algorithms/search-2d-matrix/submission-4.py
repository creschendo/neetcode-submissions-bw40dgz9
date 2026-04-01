class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bot, top = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        # first search for the row that may contain the number:
        row = 0
        while bot <= top:
            row = bot + ((top - bot) // 2)
            if target < matrix[row][left]:
                top = row - 1
            elif target > matrix[row][right]:
                bot = row + 1
            else:
                break

        # standard 1D binary search
        while left <= right:
            mid = left + ((right - left) // 2)

            if matrix[row][mid] > target:
                right = mid - 1
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                return True
        return False