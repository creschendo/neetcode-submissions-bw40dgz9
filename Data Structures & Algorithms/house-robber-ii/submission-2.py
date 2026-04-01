class Solution:
    def rob(self, nums: List[int]) -> int:
        # Run the helper function twice, once on everything except the first, 
        # and once on everything except the last
        # Account for only one house edge case
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1 = rob2 = 0

        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2