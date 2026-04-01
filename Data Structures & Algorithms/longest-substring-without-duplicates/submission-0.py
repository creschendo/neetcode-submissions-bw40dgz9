class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        left, right, sol = 0, 1, 1
        seen = set(s[0])

        while right < len(s):
            char = s[right]
            if char in seen:
                while char in seen:
                    seen.remove(s[left])
                    left += 1
            seen.add(char)
            sol = max(right - left + 1, sol)
            right += 1
        
        return sol
