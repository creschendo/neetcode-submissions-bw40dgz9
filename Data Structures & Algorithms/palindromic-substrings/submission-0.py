class Solution:
    def countSubstrings(self, s: str) -> int:
        sol = 0
        for i in range(len(s)):

            # odd palidromes
            left = right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                sol += 1
                left -= 1
                right += 1

            # even palindromes
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                sol += 1
                left -= 1
                right += 1
        
        return sol