class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = int(max(weights)), int(sum(weights))

        sol = right

        def check(cap):
            curr = 0
            d = 1
            for w in weights:
                curr += w
                if curr > cap:
                    d += 1
                    curr = w
            
            return d <= days
        
        while left <= right:
            mid = int((left + right) // 2)

            if check(mid):
                sol = min(sol, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return sol