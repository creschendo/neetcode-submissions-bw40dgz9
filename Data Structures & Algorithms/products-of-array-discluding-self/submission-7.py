class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        curr = 1
        pref = [0] * len(nums)
        for i, num in enumerate(nums):
            pref[i] = curr
            curr *= num

        curr = 1
        for j in range(len(nums) - 1, -1, -1):
            pref[j] *= curr
            curr *= nums[j]
        
        return pref

        [1, 2, 4, 6]
        pref
        [1, 1, 2, 4]
        [48, 24, 12, 1]