class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Time: O(n * n!)
        # Space: O(n * n!)
        # use a true/false array of length len(nums) to track whether each
        # number has been used in the current permutation
        sol = []
        
        def backtrack(perm, nums, pick):
            # full permutation reached, add to solution and return
            if len(perm) == len(nums):
                sol.append(perm.copy())
                return

            # iterate through every number, choosing it or not
            for i in range(len(nums)):
                if not pick[i]:
                    perm.append(nums[i])
                    pick[i] = True
                    backtrack(perm, nums, pick)
                    perm.pop()
                    pick[i] = False

        
        backtrack([], nums, [False] * len(nums))
        return sol