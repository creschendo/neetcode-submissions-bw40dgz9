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