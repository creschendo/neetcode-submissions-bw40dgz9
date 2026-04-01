class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rems = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] in rems and rems.index(nums[i]) != i:
                return [rems.index(nums[i]), i]
            else:
                rems[i] = target - nums[i]