class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for t in tokens:
            if t == "+":
                v1 = s.pop()
                v2 = s.pop()
                s.append(v1 + v2)
            elif t == "-":
                v1 = s.pop()
                v2 = s.pop()
                s.append(v2 - v1)
            elif t == "*":
                v1 = s.pop()
                v2 = s.pop()
                s.append(v2 * v1)
            elif t == "/":
                v1 = s.pop()
                v2 = s.pop()
                s.append(int(v2 / v1))
            else:
                s.append(int(t))
            print(s)
        return s[0]

"""

        ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

        (((10 * (6 / ((9 + 3) * -11))) + 17) + 5)
"""