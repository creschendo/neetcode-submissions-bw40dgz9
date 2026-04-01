class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = set(s)
        sol = 0
        for char in chars:
            count, left = 0,0

            for right in range(len(s)):
                if s[right] == char:
                    count += 1
                
                while (right - left + 1) - count > k:
                    if s[left] == char:
                        count -= 1
                    left += 1
                
                sol = max(sol, (right - left + 1))
        
        return sol
        