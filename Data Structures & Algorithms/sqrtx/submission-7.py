class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        sol = 0
        while left <= right:
            mid = (left + right) // 2
            sqr = mid * mid
            if sqr < x:
                sol = mid
                left = mid + 1
            elif sqr > x:
                right = mid - 1
            else:
                return mid
        return sol

        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]