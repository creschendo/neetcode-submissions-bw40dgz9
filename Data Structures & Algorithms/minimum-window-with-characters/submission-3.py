class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if t empty, return empty
        if t == "":
            return ""

        # count characters in target
        counts = {}
        for char in t:
            counts[char] = counts.get(char, 0) + 1


        sol = [-1, -1]
        best = float('inf')

        left = 0
        window = {}

        have = 0
        need = len(counts)
        # iterate across all possible right bounds
        for right in range(len(s)):
            # add a count to the new character added on the right
            window[s[right]] = window.get(s[right], 0) + 1

            # if the added count equals the count in target, add one to have
            if s[right] in counts and window[s[right]] == counts[s[right]]:
                have += 1
            
            # move the left bound to the right until condition isn't satisfied
            while have == need:

                # if the current substring is smaller than our best, update
                if (right - left + 1) < best:
                    best = right-left+1
                    sol = [left, right]

                # decrement count of removed left character
                window[s[left]] -= 1

                # if the removed count causes a needed character count to drop below threshold, 
                # decrement have. will terminate loop, since we can't go left anymore
                if s[left] in counts and window[s[left]] < counts[s[left]]:
                    have -= 1
                
                # move to the right
                left += 1
        
        left, right = sol
        if best != float('inf'):
            return s[left:right+1]
        return ""