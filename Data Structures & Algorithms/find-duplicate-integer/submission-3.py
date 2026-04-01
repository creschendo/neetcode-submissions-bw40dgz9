class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 
        for x in nums:
            if nums[abs(x)] < 0:
                return abs(x)
            else:
                nums[abs(x)] *= -1