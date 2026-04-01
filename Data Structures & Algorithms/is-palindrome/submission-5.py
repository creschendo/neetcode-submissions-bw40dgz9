class Solution:
    def isPalindrome(self, s: str) -> bool:

        # O(n) time
        # O(1) space

        # two pointers approach, set left and right
        left, right = 0 , len(s) - 1

        # move inwards until pointers cross
        while left < right:
            # ignore non alphanumeric on each side
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            # characters at respective positions are not equal
            # return false
            elif s[left].lower() != s[right].lower():
                print(s[left] + " not equal to  " + s[right])
                return False

            # move pointers inward
            else:
                left += 1
                right -= 1
        
        return True

      
        