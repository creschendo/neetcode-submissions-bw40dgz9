import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(bnans):
            time = h
            for pile in piles:
                time -= math.ceil(pile/bnans)
                if time < 0:
                    return False
            return True
        piles.sort()
        left, right = 1, piles[-1]
        mink = float('inf')
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
                mink = min(mink, mid)
            else:
                left = mid + 1
            

        return mink