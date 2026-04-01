class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Initialize solution and carry bits
        carry = 0
        sol = 0

        # Iterate through each bit
        for i in range(32):

            # Extract ith bit in each number
            abit = (a >> i) & 1
            bbit = (b >> i) & 1

            # Establish the current bit
            curbit = abit ^ bbit ^ carry

            # Check if there's a carry for the next bit
            carry = (abit + bbit + carry >= 2)

            # If the current bit is a one, set in solution
            if curbit:
                sol |= (1 << i)
        
        # If the solution is too large, set it to a negative
        if sol >= 0x7FFFFFFF:
            sol = ~(sol ^ 0xFFFFFFFF)   
        
        return sol