class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sol = curSum = 0
        prefix = {0: 1}

        for num in nums:
            curSum += num
            diff = curSum - k

            sol += prefix.get(diff, 0)
            prefix[curSum] = 1 + prefix.get(curSum, 0)

        return sol