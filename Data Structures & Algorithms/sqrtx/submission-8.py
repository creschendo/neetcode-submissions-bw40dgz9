class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        best = 0
        while left <= right:
            mid = (left + right) // 2

            if mid * mid < x:
                best = max(best, mid)
                left = mid + 1
            elif mid * mid > x:
                right = mid - 1
            else:
                return mid
        return best