class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(i):
            # end reached, add all palindromes to result
            if i >= len(s):
                res.append(part.copy())
                return

            # iterate through every possible cut position
            # ex: for "aab", the top level iteration would be 
            # |a|ab, |aa|b, |aab|
            # once a palindrome is found, recurse down
            # the remainder of the string to try and make additional cuts
            for j in range(i, len(s)):

                # palindrome found, recurse to see if a list is possible
                if self.isPali(s, i, j):

                    # add to part
                    part.append(s[i:j+1])

                    # recurse
                    dfs(j + 1)

                    # backtrack, try other palindromes also starting at i
                    part.pop()
        
        
        dfs(0)
        return res

    # returns whether the substring of s bound by l and r
    # is a palindrome
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True