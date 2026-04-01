class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # - We use nums[x] as a bucket representing whether x has already been seen
        # - Since we can guarantee that values lie between 1 and n, we can use the 
        #   values as indices without issue
        # - We mark nums[x] negative whenever we see x
        # - If we ever find that nums[x] is negative already, that means x is a duplicate
        for x in nums:
            if nums[abs(x)] < 0:
                return abs(x)
            else:
                nums[abs(x)] *= -1