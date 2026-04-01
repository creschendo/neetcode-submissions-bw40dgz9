class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # memo table
        # each (i, total) entry represents all possible ways to sum to
        # the target from index "i" at current total "total"
        dp = {}

        def backtrack(i, total):
            # reached end of array, check if total is target
            if i == len(nums):
                return 1 if total == target else 0

            # memo hit, just return cached result
            if (i, total) in dp:
                return dp[(i, total)]
            
            # explore both paths, subtracting and adding the current value
            # add the counts 
            dp[(i, total)] = (backtrack(i + 1, total + nums[i]) + 
                              backtrack(i + 1, total - nums[i]))

            return dp[(i, total)]
        
        return backtrack(0, 0)

"""
nums = [2, 2, 2]
target = 2
backtrack(0, 0)
    - backtrack(1, 2)
        - backtrack(2, 4)
            - backtrack(3, 6)
                - return 0 (base case)
            - backtrack(3, 2)
                - return 1 (base case)
        - backtrack(2, 0)
            -backtrack(3, 2)
                - return 1 (base case)
            - backtrack(3, -2)
                - return 0 (base case)
    - backtrack(1, -2)
        - backtrack(2, 0)
            - return 1 (memo hit)
        - backtrack (2, -4)
            - backtrack(3, -2)
                - return 0 (base case)
            - backtrack(3, -6)
                - return 0 (base case)
    

"""