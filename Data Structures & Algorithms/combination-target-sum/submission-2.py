class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol = []
        nums.sort()

        def bt(i, curr, total):
            if total == target:
                sol.append(list(curr))
                return

            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                curr.append(nums[j])
                bt(j, curr, total + nums[j])
                curr.pop()

        bt(0, [], 0)
        return sol