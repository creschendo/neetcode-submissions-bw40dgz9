class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        left = 0

        for right in range(1, len(prices)):
            profit = prices[right] - prices[left]
            if profit < 0:
                left = right
            best = max(best, profit)
        return best