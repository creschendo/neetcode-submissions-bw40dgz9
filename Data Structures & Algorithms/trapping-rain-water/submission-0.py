class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        # calculate prefix maximum
        pref = [0] * n
        premax = float("-inf")
        for i in range(n):
            curr = height[i]
            premax = max(curr, premax)
            pref[i] = premax
        
        # calculate suffix maximum
        suff = [0] * n
        sumax = float("-inf")
        for j in range(n - 1, -1, -1):
            curr = height[j]
            sumax = max(curr, sumax)
            suff[j] = sumax
        
        sol = 0
        for k in range(n):
            sol += (min(pref[k], suff[k]) - height[k])
        
        return sol