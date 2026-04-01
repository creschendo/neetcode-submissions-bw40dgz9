class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        # pref = [0, 2, 2, 3, 3, 3, 3, 3, 3, 3]
        pref = [0] * n
        premax = float('-inf')
        for i in range(n):
            premax = max(height[i], premax)
            pref[i] = premax
        
        # suff = [3, 3, 3, 3, 3, 3, 3, 3, 2, 1]
        suff = [0] * n
        suffmax = float('-inf')
        for i in range(n-1, -1, -1):
            suffmax = max(height[i], suffmax)
            suff[i] = suffmax
        

        sol = 0
        # + 0, 0, 2, 0, 2, 3, 2, 0, 0 = 9
        for i in range(n):
            sol += (min(pref[i], suff[i]) - height[i])

        return sol