class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [0] * len(nums)
        val = 1
        for i in range(len(nums)):
            pref[i] = val
            val *= nums[i]
        
        val = 1
        for i in range(len(nums) - 1, -1, -1):
            pref[i] *= val
            val *= nums[i]

        return pref