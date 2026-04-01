class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        pref = [0] * n
        premax = float('-inf')
        for i in range(n):
            premax = max(height[i], premax)
            pref[i] = premax

        suff = [0] * n
        suffmax = float('-inf')
        for i in range(n-1, -1, -1):
            suffmax = max(height[i], suffmax)
            suff[i] = suffmax
        
        sol = 0
        for i in range(n):
            sol += (min(pref[i], suff[i]) - height[i])

        return sol