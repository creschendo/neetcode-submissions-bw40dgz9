class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        window = set()
        sol = 0
        while right < len(s):
            val = s[right]
            while val in window:
                window.remove(s[left])
                left += 1
            window.add(val)
            sol = max(sol, right - left + 1)
            right += 1
        return sol