class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sol = float("-inf")
        cur = 0

        for num in nums:
            cur = max(num, cur + num)
            sol = max(sol, cur)
        
        return sol