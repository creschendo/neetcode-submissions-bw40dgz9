class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # create new result array
        res = [1] * len(nums)

        # compute prefix prod
        curr = 1
        pref = [1] * len(nums)
        for i in range(len(nums)):
            pref[i] = curr
            curr *= nums[i]
        print(pref)
        # compute suffix prod
        curr = 1
        for i in range(len(nums) - 1, -1, -1):
            pref[i] = curr * pref[i]
            curr *= nums[i]
        return pref