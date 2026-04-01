class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # initialize pointer and carry variables at the end
        # start carry at one since we need to add 1
        pointer, carry = len(digits) - 1, 1

        # stop when we get to the end, or nothing to carry     
        while pointer >= 0 and carry:

            # add to digit
            val = digits[pointer] + carry

            # greater than 9, need to carry
            if val > 9:
                carry = 1

            # less than 10, no carry
            else:
                carry = 0

            # reassign the digit, works for 1 and 2 digits
            digits[pointer] = val % 10

            # decrement the pointer
            pointer -= 1
        
        # insert to beginning if carry left over at the end
        if carry:
            digits.insert(0, 1)
        return digits
