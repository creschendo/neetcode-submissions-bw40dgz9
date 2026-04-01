class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #    a  c  e 
        # a [0, 0, 0, 0]
        # b [0, 0, 0, 0]
        # c [0, 0, 0, 0]
        # d [0, 0, 0, 0]
        # e [0, 0, 0, 0]
        #   [0, 0, 0, 0]


        # initialize m + 1 by n + 1 array of zeroes, where m is the length of text1, and n
        # is the length of text2
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                # characters match, so add one to diagonal result
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                
                # characters don't match, so set to max of decisions
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        # return result
        return dp[0][0]