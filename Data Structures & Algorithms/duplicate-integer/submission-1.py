class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # just return if a hashset has a different length than original set
        # if it does, at least one duplicate exists
        # if not, no duplicates
        return len(set(nums)) != len(nums)