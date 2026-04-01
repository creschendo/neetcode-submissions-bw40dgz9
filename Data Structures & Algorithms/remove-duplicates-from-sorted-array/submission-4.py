class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        rep = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            nums[rep] = nums[i]
            rep += 1
        return rep