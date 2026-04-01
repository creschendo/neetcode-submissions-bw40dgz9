class Solution:
    def trap(self, height: List[int]) -> int:
        pref = [0] * len(height)
        suff = [0] * len(height)

        curr = 0
        for i, num in enumerate(height):
            pref[i] = curr
            curr = max(curr, num)
        
        curr = 0
        for i in range(len(height) - 1, -1, -1):
            suff[i] = curr
            curr = max(curr, height[i])
        

        sol = 0
        for i in range(len(height)):    
            left, right = pref[i], suff[i]
            sol += (max(0, min(left, right) - height[i]))
        return sol