class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[m-1][n-1] = 1
        print(dp[m-1][n-1])
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue
                right, down = 0, 0
                if j + 1 < n:
                    print(j)
                    right += dp[i][j+1]
                if i + 1 < m:
                    down += dp[i + 1][j]
                dp[i][j] = right + down
        
        return dp[0][0]