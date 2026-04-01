class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                prof += prices[i + 1] - prices[i]
        return prof