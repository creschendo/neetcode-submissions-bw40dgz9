class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        for i in range(len(prices) - 1):
            val = prices[i + 1] - prices[i]
            if val > 0:
                prof += val
        return prof