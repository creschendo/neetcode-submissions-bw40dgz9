class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def backtrack(i, curr):
            nonlocal res
            res += curr

            for j in range(i, len(nums)):
                curr ^= nums[j]
                backtrack(j + 1, curr)
                curr ^= nums[j]

        backtrack(0, 0)
        return res
