class Solution:
    def trap(self, height: List[int]) -> int:
        pref = []
        curr = 0
        for h in height:
            pref.append(curr)
            curr = max(curr, h)
        
        suff = [0] * len(height)
        curr = 0
        for i in range(len(height) - 1, -1, -1):
            suff[i] = curr
            curr = max(curr, height[i])
        print(pref)
        print(suff)
        sol = 0
        for i in range(len(height)):
            print("i:" + str(i))
            water = max(0, min(pref[i], suff[i]) - height[i])
            print("water:" + str(water))
            sol += water
        return sol