class Solution:
    def countBits(self, n: int) -> List[int]:
        # create dp array of all zeroes
        dp = [0] * (n + 1)

        # the highest bit position we reach
        offset = 1

        for i in range(1, n + 1):
            # check if a new offset is necessary
            if offset * 2 == i:
                offset = i

            # add 1 to previous answers
            dp[i] = 1 + dp[i - offset]

        return dp

    """
    Intuition:
        offset = 1
    0 = 0000 = 0
    1 = 0001 = 1
        offset = 2
    2 = 0010 = 1 + dp[n - 2] = 1
    3 = 0011 = 1 + dp[n - 2] = 2
        offset = 4
    4 = 0100 = 1 + dp[n - 4] = 1
    5 = 0101 = 1 + dp[n - 4] = 2
    """
