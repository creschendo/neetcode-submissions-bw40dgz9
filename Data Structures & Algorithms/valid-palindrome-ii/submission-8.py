class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPalin(string):
            left, right = 0, len(string) - 1

            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return isPalin(s[left + 1: right + 1]) or isPalin(s[left:right])
            left += 1
            right -= 1
            
        return True