class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []

        #O(n) time
        #O(n) space
        
        # add all alphanumeric characters to a list in lowercase
        for char in s:
            if char.isalnum():
                res.append(char.lower())
        
        # return if they are the same forwards and backwards
        return res == res[::-1]
        