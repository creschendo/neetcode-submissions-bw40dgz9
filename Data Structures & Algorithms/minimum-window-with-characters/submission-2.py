class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        counts = {}
        for char in t:
            counts[char] = counts.get(char, 0) + 1

        sol = [-1, -1]
        best = float('inf')

        left = 0
        window = {}

        have = 0
        need = len(counts)

        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1

            if s[right] in counts and window[s[right]] == counts[s[right]]:
                have += 1
            
            while have == need:
                if (right - left + 1) < best:
                    best = right-left+1
                    sol = [left, right]
                window[s[left]] -= 1

                if s[left] in counts and window[s[left]] < counts[s[left]]:
                    have -= 1
                
                # move to the right
                left += 1
                
        left, right = sol
        if best != float('inf'):
            return s[left:right+1]
        return ""