class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}

        left = 0
        maxLen = 0
        freq = 0
        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            freq = max(freq, counts.get(s[right]))

            while (right - left + 1) - freq > k:
                counts[s[left]] -= 1
                left += 1

            maxLen = max(maxLen, right - left + 1)
        return maxLen