class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j, profit = 0, 1, 0
        while j < len(prices):
            val = prices[j] - prices[i]
            if val < 0:
                i = j
            profit = max(val, profit)
            j += 1

        return profit

            
