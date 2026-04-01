class Solution:
    def trap(self, height: List[int]) -> int:
        # height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]

        # [0, 0, 2, 2, 3, 3, 3, 3, 3, 3]
        pref = []
        curr = 0
        for h in height:
            pref.append(curr)
            curr = max(curr, h)
        

        # [3, 3, 3, 3, 3, 3, 3, 2, 1, 0]
        suff = [0] * len(height)
        curr = 0
        for i in range(len(height) - 1, -1, -1):
            suff[i] = curr
            curr = max(curr, height[i])

        # [0, 0, 2, 0, 2, 3, 2, 0, 0, 0] = 9
        sol = 0
        for i in range(len(height)):
            print("i:" + str(i))
            water = max(0, min(pref[i], suff[i]) - height[i])
            print("water:" + str(water))
            sol += water
        return sol