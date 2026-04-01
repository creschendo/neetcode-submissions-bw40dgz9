class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()

        # create a memo table
        # rows represent using up to coins i
        # columns represent values leading up to amount
        # memo[i][j] represents all ways to make up j amount with
        # coins up to an including coin i
        memo = [[-1] * (amount + 1) for _ in range(len(coins) + 1)]

        def dfs(i, a):
            # one way to make amt 0
            if a == 0:
                return 1
            
            # out of bounds, 0 ways
            if i >= len(coins):
                return 0
            
            # value computed already, just return
            if memo[i][a] != -1:
                return memo[i][a]

            res = 0
            # check if we can use current coin value
            if a >= coins[i]:
                # find number of ways if we don't use current coin
                res = dfs(i + 1, a)

                # find number of ways if we use current coin
                res += dfs(i, a - coins[i])

            # set memo value
            memo[i][a] = res
            return res

        return dfs(0, amount)