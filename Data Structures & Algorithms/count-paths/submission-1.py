class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # Create an empty matrix of size m x n
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # Fill in the destination square to 1
        dp[m-1][n-1] = 1

        # Iterate from bottom right to top left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                # Skip the bottom right square
                if i == m - 1 and j == n - 1:
                    continue
                right, down = 0, 0

                # If right is in bounds, add right result
                if j + 1 < n:
                    print(j)
                    right += dp[i][j+1]
                
                # If down is in bounds, add down result
                if i + 1 < m:
                    down += dp[i + 1][j]
                
                # Add total number of ways to reach goal
                dp[i][j] = right + down
        
        # Base square will contain total count of all possible paths
        return dp[0][0]