class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        sol = [0] * (2 * len(nums))

        for i in range(len(nums)):
            sol[i] = nums[i]
            sol[i + len(nums)] = nums[i]
        return sol