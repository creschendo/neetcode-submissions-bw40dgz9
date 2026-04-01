class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Minimize k
        # The upper bound of k is max(piles), meaning eating the largest number
        # of bananas each hour will guarantee a valid result.
        # Thus, we find max and use binary search to search between 1 and max(piles)
        # A valid mid value means we may go lower, while invalid means we must go up.
        maxk = sol = max(piles)
        left, right = 1, maxk
        while left <= right:
            # new mid value
            mid = (left + right) // 2

            # check if mid is a valid result, i.e. will we finish 
            # the bananas on time
            valid = True
            hours = 0
            for pile in piles:
                # integer ceiling division trick
                # ceiling(pile/k)
                hours += (pile + mid - 1) // mid
                if hours > h:
                    valid = False
                    break

            # valid, go left
            if valid:
                sol = min(mid, sol)
                right = mid - 1
            # invalid, go right
            else:
                left = mid + 1
        return sol