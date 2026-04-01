class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        dp = {}
        def dfs(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            if (i, j) in dp:
                return dp[(i, j)]

            if word1[i] == word2[j]:
                dp[(i, j)] = dfs(i + 1, j + 1)
            else:
                res = min(dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1))
                dp[(i, j)] = res + 1
            return dp[(i, j)]

        return dfs(0, 0)
        """
        dp = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

        # fill out right column for deletions
        # (out of word2 letters, so remaining ops # is len(w1) - i)
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i
        
        # fill bottom row for insertions
        # (out of word1 letters, so remaining ops # is len(w2) - j)
        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j

        # go from right to left, bottom to top
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):

                # two characters are the same, no edits needed so 
                # operation count is the same as the cost to edit the rest
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]

                # characters aren't the same, so 1 edit is required
                # pick the state from either insertion, deletion, or replacement
                # which yields the fewest future operations and add 1 for this edit
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])

        return dp[0][0]

        """