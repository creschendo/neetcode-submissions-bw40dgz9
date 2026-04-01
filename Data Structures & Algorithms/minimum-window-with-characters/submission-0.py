class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # the target is empty, so nothing can contain it
        if t == "":
            return ""

        # count up all frequencies of unique characters in target
        counts = {}
        for char in t:
            counts[char] = counts.get(char, 0) + 1
        
        # keep track of solution indices and length
        sol = [-1, -1]
        best = float('inf')

        # start left, start counting all characters
        left = 0
        window = {}

        # keep track of satisfied characters
        have = 0

        # number of characters to satisfy
        need = len(counts)


        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1

            if s[right] in counts and window[s[right]] == counts[s[right]]:
                have += 1
            
            while have == need:
                if (right - left + 1) < best:
                    best = (right - left + 1)
                    sol = [left, right]
                
                window[s[left]] -= 1
                if s[left] in counts and window[s[left]] < counts[s[left]]:
                    have -= 1
                left += 1
        left, right = sol
        if best != float('inf'):
            return s[left : right + 1]
        return ""
        