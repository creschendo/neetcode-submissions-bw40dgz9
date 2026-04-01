class Solution:

    def encode(self, strs: List[str]) -> str:
        coded = []
        for string in strs:
            coded.append(str(len(string)) + "#" + string)
        return "".join(coded)
    def decode(self, s: str) -> List[str]:
        decoded = []
        i, j = 0, 1
        while j < len(s):
            while s[j] != "#":
                j += 1
            length = s[i:j]
            j += 1
            i = j
            j += int(length)
            decoded.append(s[i:j])
            i = j
        return decoded
