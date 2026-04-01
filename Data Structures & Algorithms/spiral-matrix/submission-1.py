class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bot, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        sol = []
        
        while top <= bot and left <= right:
            # top row
            for i in range(left, right + 1):
                sol.append(matrix[top][i])
            top += 1

            # right column
            for j in range(top, bot + 1):
                sol.append(matrix[j][right])
            right -= 1

            # bottom row
            if top <= bot:
                for k in range(right, left - 1, -1):
                    sol.append(matrix[bot][k])
                bot -= 1

            # left column
            if left <= right:
                for l in range(bot, top - 1, -1):
                    sol.append(matrix[l][left])
                left += 1

        return sol
