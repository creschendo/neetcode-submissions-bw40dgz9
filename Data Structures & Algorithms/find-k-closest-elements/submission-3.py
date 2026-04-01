class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort()

        # find the optimal center first
        opt = 0
        best = float('inf')
        for i in range(len(arr)):
            if abs(arr[i] - x) < best:
                opt = i
                best = abs(arr[i] - x)
        

        # expand outwards k - 1 times to get a k sized window
        left, right = opt, opt
        for _ in range(k - 1):
            dLeft = dRight = float('inf')

            if left - 1 >= 0:
                dLeft = abs(arr[left - 1] - x)
            
            if right + 1 < len(arr):
                dRight = abs(arr[right + 1] - x)

            if dLeft <= dRight:
                left -= 1
            else:
                right += 1
        
        return arr[left:right + 1]
