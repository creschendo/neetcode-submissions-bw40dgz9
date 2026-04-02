class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []

        def bt(i, curr):
            sol.append(list(curr))

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                curr.append(nums[j])
                bt(j + 1, curr)
                curr.pop()

        bt(0, [])
        return sol