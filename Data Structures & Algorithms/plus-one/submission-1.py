class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # initialize pointer and carry variables at the end
        # start carry at one since we need to add 1
        pointer, carry = len(digits) - 1, 1

        # stop when we get to the end, or carry       
        while pointer >= 0:
            val = digits[pointer] + carry
            if val > 9:
                carry = 1
            else:
                carry = 0
            digits[pointer] = val % 10
            pointer -= 1
        if carry:
            digits.insert(0, 1)
        return digits
