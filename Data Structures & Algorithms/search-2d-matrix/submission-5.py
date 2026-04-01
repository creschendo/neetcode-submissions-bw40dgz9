class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        top, bot = 0, m - 1

        while top <= bot:
            mid = (top + bot) // 2
            l, r = matrix[mid][0], matrix[mid][n-1]
            if target < l:
                bot = mid - 1
            elif target > r:
                top = mid + 1
            else:
                break
        
        left, right = 0, n - 1
        while left <= right:
            midd = (left + right) // 2
            val = matrix[mid][midd]
            if target < val:
                right = midd - 1
            elif target > val:
                left = midd + 1
            else:
                return True
        
        return False
