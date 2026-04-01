class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        sol = right
        while left <= right:
            mid = int((left + right) // 2)

            # check if w works
            d = 1
            curr = 0
            for w in weights:
                curr += w
                if curr > mid:
                    d += 1
                    curr = w

            # w works, set solution and try lower weight
            if d <= days:
                sol = min(sol, mid)

                right = mid - 1
            
            # w doesn't work, try higher weight
            else:
                left = mid + 1

        return sol
                