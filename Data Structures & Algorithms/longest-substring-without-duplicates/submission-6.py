class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seen = set(s[0])
        left, right, sol = 0, 1, 1
        while right < len(s):
            char = s[right]

            while char in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(char)
            sol = max(sol, right - left + 1)
            right += 1
        return sol