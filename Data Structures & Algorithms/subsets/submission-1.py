class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []
        def bt(i, subset):
            sol.append(list(subset))  # collect here, no base case needed

            for j in range(i, len(nums)):
                subset.append(nums[j])
                bt(j + 1, subset)
                subset.pop()

        bt(0, [])
        return sol