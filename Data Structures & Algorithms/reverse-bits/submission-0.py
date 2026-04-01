class Solution:
    def reverseBits(self, n: int) -> int:
        sol = 0

        for i in range(32):
            if ((n >> i) & 1):
                sol |= (1 << (31 - i))
        
        return sol
