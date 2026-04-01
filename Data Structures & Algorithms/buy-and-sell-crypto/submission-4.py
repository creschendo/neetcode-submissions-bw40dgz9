class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        maxProfit = 0
        left = 0

        for right in range(len(prices)):
            profit = prices[right] - prices[left]
            if profit < 0:
                left = right
            else:
                maxProfit = max(maxProfit, profit)
        
        return maxProfit