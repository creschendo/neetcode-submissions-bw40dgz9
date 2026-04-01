class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pointer, carry = len(digits) - 1, 1
        while pointer >= 0:
            val = digits[pointer] + carry
            if val > 9:
                carry = 1
            else:
                carry = 0
            digits[pointer] = val % 10
            if not carry:
                break
            pointer -= 1
        if carry:
            digits.insert(0, 1)
        return digits
