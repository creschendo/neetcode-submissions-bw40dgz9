class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        # check if it's possible to split into <= k subarrays
        # where the largest sum is <= largest
        def canSplit(largest):
            subarray = 1
            curSum = 0
            for num in nums:
                curSum += num
                if curSum > largest:
                    subarray += 1
                    if subarray > k:
                        return False
                    curSum = num
            return True


        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            mid = (l + r) // 2

            # if you can split at this sum, check 
            # for a smaller one on the left
            if canSplit(mid):
                res = mid
                r = mid - 1

            # invalid sum split, go right
            else:
                l = mid + 1
        return res