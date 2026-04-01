class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ptr = 0

        while ptr <= (len(s) - 1) // 2:

            s[ptr], s[(len(s) - 1) - ptr] = s[(len(s) - 1) - ptr], s[ptr]

            ptr += 1
        