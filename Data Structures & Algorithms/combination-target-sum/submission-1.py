class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol = []

        def helper(i, cur, total):
            if total == target:
                sol.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            cur.append(nums[i])
            helper(i, cur, total + nums[i])

            cur.pop()
            helper(i + 1, cur, total)
        helper(0, [], 0)
        return sol
        