class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rems = [float('inf')] * len(nums)

        for i, num in enumerate(nums):
            rem = target-num
            if rem in rems:
                return [rems.index(rem), i]
            else:
                rems[i] = num
        