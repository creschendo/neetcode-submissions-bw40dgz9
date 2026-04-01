class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # create a set of all distinct characters
        chars = set(s)
        sol = 0

        # for each distinct character, iterate over the entire string
        for char in chars:
            count, left = 0,0

            # iterate through all possible right bounds
            for right in range(len(s)):

                # count the number of occurences of the current character
                if s[right] == char:
                    count += 1
                
                # calculate the number of swaps and move the left
                # bound right until at most k swaps 
                while (right - left + 1) - count > k:

                    # if the left bound we move over is the char,
                    # subtract from the count
                    if s[left] == char:
                        count -= 1

                    # move left to the right
                    left += 1
                
                # we've found the maximum possible length at this right bound
                # with the current character. replace sol if longer
                sol = max(sol, (right - left + 1))
        
        return sol
        