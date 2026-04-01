class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, sol = 0, 0, 0
        seen = set()

        while right < len(s):
            char = s[right]
            if char not in seen:
                seen.add(char)
                right += 1
            else:
                while char in seen:
                    rem = s[left]
                    seen.remove(rem)
                    left += 1
            sol = max(sol, right - left)
        return sol