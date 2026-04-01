class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        left, right = 0, length - 1

        l, r = 1, length - 2
        while l <= r:
            m = (l + r) // 2
            left, mid, right = mountainArr.get(m - 1), mountainArr.get(m), mountainArr.get(m + 1)
            if left < mid < right:
                l = m + 1
            elif left > mid > right:
                r = m - 1
            else:
                break
        peak = m

        best = float('inf')
        # search left side
        left, right = 0, peak - 1
        while left <= right:
            mid = (left + right) // 2
            val = mountainArr.get(mid)
            if val < target:
                left = mid + 1
            elif val > target:
                right = mid - 1
            else:
                return mid
        
        # search right side
        left, right = peak, length - 1
        while left <= right:
            mid = (left + right) // 2
            val = mountainArr.get(mid)
            if val < target:
                right = mid - 1
            elif val > target:
                left = mid + 1
            else:
                return mid
        return  -1
