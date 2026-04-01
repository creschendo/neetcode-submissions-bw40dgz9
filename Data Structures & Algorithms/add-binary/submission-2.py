class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ap, bp = len(a) - 1, len(b) - 1
        carry = 0
        sol = ["0"] * max(len(a), len(b))
        ptr = len(sol) - 1
        while ap >= 0 or bp >= 0:
            adigit = int(a[ap]) if ap >= 0 else 0
            bdigit = int(b[bp]) if bp >= 0 else 0

            val = adigit + bdigit + carry

            carry = (val >= 2)

            sol[ptr] = str(val % 2)

            ap -= 1
            bp -= 1
            ptr -= 1

        if carry:
            sol.insert(0, "1")

        return "".join(sol)
