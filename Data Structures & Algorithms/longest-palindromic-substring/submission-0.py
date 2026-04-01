class Solution:
    def longestPalindrome(self, s: str) -> str:
        index = length = 0

        for i in range(len(s)):

            # odd palidromes
            left = right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > length:
                    index = left
                    length = right - left + 1
                left -= 1
                right += 1

            # even palindromes
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > length:
                    index = left
                    length = right - left + 1
                left -= 1
                right += 1
        
        return s[index : index + length]