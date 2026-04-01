class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.helper(n)
        while slow != fast:
            fast = self.helper(self.helper(fast))
            slow = self.helper(slow)
        return True if fast == 1 else False
    def helper(self, n):
        output = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output