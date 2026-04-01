class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxk = sol = max(piles)
        left, right = 1, maxk
        while left <= right:
            mid = (left + right) // 2
            valid = True
            hours = 0
            for pile in piles:
                # integer ceiling division trick
                # ceiling(pile/k)
                hours += (pile + mid - 1) // mid
                if hours > h:
                    valid = False
                    break
            if valid:
                sol = min(mid, sol)
                right = mid - 1
            else:
                left = mid + 1
        return sol