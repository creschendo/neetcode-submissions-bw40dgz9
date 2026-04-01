class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [0] * len(nums)
        curr = 1
        for i in range(len(nums)):
            pref[i] = curr
            curr *= nums[i]
        
        curr = 1
        for i in range(len(nums) - 1, -1, -1):
            pref[i] *= curr
            curr *= nums[i]
        
        return pref