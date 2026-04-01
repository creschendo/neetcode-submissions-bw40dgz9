class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # first sort nums, include step include the number and 
        # all duplicates, exclude step skip ahead to next unique 
        # value

        sol = []
        subset = []
        nums.sort()
        def dfs(i):
            # full subset found
            if i >= len(nums):
                sol.append(subset.copy())
                return
            
            # include the current number and recurse
            subset.append(nums[i])
            dfs(i + 1)

            # remove current
            subset.pop()

            # skip ahead to avoid duplicate subsets and recurse on 
            # exclusion step
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)

        dfs(0)
        return sol