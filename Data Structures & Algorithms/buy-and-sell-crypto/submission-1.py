class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy day, sell day, max profit
        i, j, profit = 0, 1, 0\
        
        # iterate through all days
        while j < len(prices):
            # the current return if we buy at
            # day i and sell at day j
            val = prices[j] - prices[i]

            # we've found a lower price than curr, 
            # so it's more optimal to buy at that price
            # since it could yield a higher profit later
            if val < 0:
                i = j

            # update max
            profit = max(val, profit)

            # increment sell day
            j += 1

        return profit

            
