class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        # append the length of the word, the separator, and the string
        for st in strs:
            res += str(len(st))
            res += "@"
            res += st
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i + 1

            # grab the full length of the string, if multiple digits
            while s[j] != "@":
                j += 1
            length = int(s[i:j])

            # move indexes to get word
            i = j + 1
            j = i + length

            # append word to result
            res.append(s[i:j])

            # move to next word's length start
            i = j
        
        #return result
        return res