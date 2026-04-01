class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        counts = defaultdict(int)
        best = 0
        for right in range(len(s)):
            
            counts[s[right]] += 1
            print(max(counts))
            while (right - left + 1) - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)
        return best