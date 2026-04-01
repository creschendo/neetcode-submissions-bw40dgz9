class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        # recurse on every possible option, using memoization to 
        # store already computed values
        def dfs(i, buying):
            # if the day is out of bounds, no profit can be made
            if i >= len(prices):
                return 0
            
            # result already exists, just return
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            # holding no coin, can buy or skip
            if buying:
                # profit from buying on current day
                buy = dfs(i + 1, False) - prices[i]

                # profit from skipping and buying on another day
                cooldown = dfs(i + 1, True)

                # store maximum profit
                dp[(i, buying)] = max(buy, cooldown)

            # holding a coin, can sell or skip
            else:
                # profit from selling on the current day
                # skip next day for cooldown
                sell = dfs(i + 2, True) + prices[i]

                # profit from holding and selling another day
                cooldown = dfs(i + 1, False)

                # store maximum profit
                dp[(i, buying)] = max(sell, cooldown)
            
            return dp[(i, buying)]
        
        return dfs(0, True)