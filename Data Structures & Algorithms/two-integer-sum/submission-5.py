class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rems = [0] * len(nums)

        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in rems and rems.index(rem) != i:
                return [rems.index(rem), i]
            else:
                print(i)
                rems[i] = nums[i]