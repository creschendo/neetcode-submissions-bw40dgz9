class Solution:
    def decodeString(self, s: str) -> str:
        self.i = 0

        def helper():
            res = ""
            k = 0

            while self.i < len(s):
                char = s[self.i]

                if char.isdigit():
                    k = k * 10 + int(char)
                elif char == "[":
                    self.i += 1
                    res += k * helper()
                    k = 0
                elif char == "]":
                    return res
                else:
                    res += char
                
                self.i += 1

            return res
        
        return helper()
"""
s="2[a3[b]]c"

helper()
i = 0, ("2")
k = 0 * 10 + 2 = 2

i = 1 ("[")
    helper()
    i = 2 ("a")
    res = "a"
    i = 3 ("3")
    k = 0 * 10 + 3 = 3
    i = 4 ("[")
        helper()
        i = 5 ("b")
        res = "b"
        i = 6 ("]")
        return res = "b"
    res += 3 * "b" = "abbb"
    i = 7 ("]")
    return "abbb"
res += 2 * "abbb" = "abbbabbb"
i = 8 ("c")
res += "c" = "abbbabbbc"

return "abbbabbbc"
"""

