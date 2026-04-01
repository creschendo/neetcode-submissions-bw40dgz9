class Solution:

    def encode(self, strs: List[str]) -> str:
        sol = ""
        for string in strs:
            sol += str(len(string))
            sol += "#"
            sol += string
        return sol
    def decode(self, s: str) -> List[str]:
        sol = []
        left, right = 0, 0

        while right < len(s):
            # move right pointer to end of length
            while s[right] != "#":
                right += 1

            # store string length
            length = s[left:right]

            left = right + 1
            right = left + int(length)
            sol.append(s[left:right])
            left = right
        return sol


