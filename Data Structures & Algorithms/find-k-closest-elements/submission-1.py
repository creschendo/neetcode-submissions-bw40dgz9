class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        best = 0
        dist = float('inf')
        for i in range(len(arr)):
            if abs(arr[i] - x) < dist:
                dist = abs(arr[i] - x)
                best = i
        print(best)
        left, right = best, best
        for _ in range(k - 1):
            dleft = float('inf')
            dright = float('inf')

            if left - 1 >= 0:
                dleft = abs(arr[left - 1] - x)

            if right + 1 < len(arr):
                dright = abs(arr[right + 1] - x)

            if dleft <= dright:
                left -= 1
            else:
                right += 1

        return arr[left:right + 1]
        

