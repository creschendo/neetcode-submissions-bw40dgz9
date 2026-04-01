class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        sol = 0
        left, freq = 0, 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0)  + 1
            freq = max(freq, count[s[right]])

            while (right - left + 1) - freq > k:
                count[s[left]] -= 1
                left += 1
            
            sol = max(sol, right- left + 1)
        return sol