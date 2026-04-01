class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rems = {}

        for i, n in enumerate(nums):
            rem = target - n
            if rem in rems:
                return [rems[rem], i]
            else:
                rems[n] = i