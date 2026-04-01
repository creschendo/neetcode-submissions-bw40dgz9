class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol = []
        nums.sort()

        def bt(i, curr, total):
            if total == target:
                sol.append(list(curr))
                return

            for j in range(i, len(nums)):
                # only positives, prune invalid branches early
                if total + nums[j] > target:
                    return

                # use current value
                curr.append(nums[j])

                # use j instead of j + 1 to reuse current value
                bt(j, curr, total + nums[j])

                # remove explored value
                curr.pop()

        bt(0, [], 0)
        return sol