class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []
        def bt(i, subset):
            if i >= len(nums):
                sol.append(list(subset))  # collect here, no base case needed
                return

            subset.append(nums[i])
            bt(i + 1, subset)
            subset.pop()
            bt(i + 1, subset)

        bt(0, [])
        return sol