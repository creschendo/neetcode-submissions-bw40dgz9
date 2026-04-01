class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1

        while left <= (len(s) - 1) // 2:
            temp = s[left]
            s[left] = s[(len(s) - 1) - left]
            s[(len(s) - 1) - left] = temp
            left += 1
        