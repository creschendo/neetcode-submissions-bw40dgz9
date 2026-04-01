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

        # iterate over all characters
        for right in range(len(s)):

            # add count to current character
            window[s[right]] = window.get(s[right], 0) + 1

            # if the current character is a target character, 
            # and we have the correct amount, add one to satisfied chars
            if s[right] in counts and window[s[right]] == counts[s[right]]:
                have += 1
            
            # shorten the left side until you cant anymore
            while have == need:

                # update solution if possible
                if (right - left + 1) < best:
                    best = (right - left + 1)
                    sol = [left, right]
                
                # subtract a count from the character leaving the window
                window[s[left]] -= 1

                # if it was a target character, check if a requirement is lost
                if s[left] in counts and window[s[left]] < counts[s[left]]:
                    have -= 1
                
                # move to the right
                left += 1
        
        # return solution
        left, right = sol
        if best != float('inf'):
            return s[left : right + 1]
        return ""
        