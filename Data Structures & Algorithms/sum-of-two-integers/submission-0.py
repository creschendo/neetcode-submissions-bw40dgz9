class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        sol = 0

        for i in range(32):
            abit = (a >> i) & 1
            bbit = (b >> i) & 1
            curbit = abit ^ bbit ^ carry
            carry = (abit + bbit + carry >= 2)
            if curbit:
                sol |= (1 << i)
        
        if sol >= 0x7FFFFFFF:
            sol = ~(sol ^ 0xFFFFFFFF)   
        
        return sol