class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0

        for i in range(len(prices) - 1):
            prof = prices[i + 1] - prices[i]
            if prof > 0:
                total += prof
        
        return total