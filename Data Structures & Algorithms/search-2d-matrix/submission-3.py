class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bot, top = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        # first search for the row that may contain the number:
        midrow = 0
        while bot <= top:
            midrow = bot + ((top - bot) // 2)
            if target < matrix[midrow][left]:
                top = midrow - 1
            elif target > matrix[midrow][right]:
                bot = midrow + 1
            else:
                break
        
        print(midrow)
        # standard 1D binary search
        while left <= right:
            mid = left + ((right - left) // 2)

            if matrix[midrow][mid] > target:
                right = mid - 1
            elif matrix[midrow][mid] < target:
                left = mid + 1
            else:
                return True
        return False