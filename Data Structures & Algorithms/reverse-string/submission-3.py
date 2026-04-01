class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for ptr in range(((len(s) - 1) // 2) + 1):
            s[ptr], s[(len(s) - 1) - ptr] = s[(len(s) - 1) - ptr], s[ptr]

        