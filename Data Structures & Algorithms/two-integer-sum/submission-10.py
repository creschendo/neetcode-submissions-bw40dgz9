class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rems = {}

        for i, num in enumerate(nums):
            rem = target-num
            if rem in rems:
                return [rems[rem], i]
            else:
                rems[num] = i
        