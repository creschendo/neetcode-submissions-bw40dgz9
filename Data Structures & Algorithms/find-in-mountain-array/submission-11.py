class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()

        left, right = 0, length - 1

        # find peak
        while left < right:
            mid = (left + right) // 2

            if mountainArr.get(mid) > mountainArr.get(mid + 1):
                right = mid
            else:
                left = mid + 1
        peak = left

        # search left side (ascending)
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
        
        # search right side (descending)
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
