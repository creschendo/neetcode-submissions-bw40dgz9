class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def helper(string):
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
                return helper(s[left + 1:right + 1]) or helper(s[left:right])
            left += 1
            right -= 1

        return True