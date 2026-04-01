class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        # left pointer, right pointer, longest length
        left, right, sol = 0, 1, 1

        # set of seen characters for the current window
        seen = set(s[0])

        while right < len(s):
            # check the newest addition
            char = s[right]

            # if already in the window, cut off 
            # characters at the left until no repeats
            if char in seen:
                while char in seen:
                    seen.remove(s[left])
                    left += 1

            # add the new character
            seen.add(char)

            # update the max length
            sol = max(right - left + 1, sol)

            # move to the next character
            right += 1
        
        return sol
