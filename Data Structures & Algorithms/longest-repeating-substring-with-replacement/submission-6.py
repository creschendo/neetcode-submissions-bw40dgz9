class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        sol = 0
        left = 0
        maxf = 0

        for right in range(len(s)):
            # count the new character coming in on the rightr
            count[s[right]] = count.get(s[right], 0) + 1

            # updated the count of the most frequent character
            maxf = max(maxf, count[s[right]])

            # the window is invalid if the number of non most frequent 
            # characters in the window is greater than k, i.e. too many swaps
            # so shrink the window on the left until it's valid
            while (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1

            # compare new valid window with current max, update if bigger
            sol = max(sol, right - left + 1)
        
        return sol