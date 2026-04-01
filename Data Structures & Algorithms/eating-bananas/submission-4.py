class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def check(b, h):
            for p in piles:
                h -= math.ceil(p/b)
            return h >= 0 
        sol = 0
        left, right = 1, max(piles)
        while left <= right:
            mid = (left + right) // 2

            if check(mid, h):
                sol = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return sol