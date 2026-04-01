class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def backtrack(current):
            if len(current) == len(nums):
                res.append(list(current))
                return
            
            for i, num in enumerate(nums):
                if used[i]:
                    continue
                if i and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                current.append(num)
                used[i] = True
                backtrack(current)
                current.pop()
                used[i] = False
        nums.sort()
        backtrack([])
        return res

        