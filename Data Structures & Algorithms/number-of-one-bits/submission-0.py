class Solution:
    def hammingWeight(self, n: int) -> int:
        sol = 0
        while n:
            if n & 1:
                sol += 1
            n >>= 1
        return sol