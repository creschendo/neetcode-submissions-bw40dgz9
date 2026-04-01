class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        # the result will be (m + n) or (m + n - 1) digits
        res = [0] * (len(num1) + len(num2))

        # reverse both strings
        num1, num2 = num1[::-1], num2[::-1]

        # iterate across all pairs
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):

                # current product of two digits
                digit = int(num1[i1]) * int(num2[i2])

                # add product to correct slot
                res[i1 + i2] += digit

                # add carry to next slot 
                res[i1 + i2 + 1] += res[i1 + i2] // 10

                # keep only ones digit for current product
                res[i1 + i2] = res[i1 + i2] % 10

        # reverse the result back to normal
        res, beg = res[::-1], 0

        # check for leading zeroes, (m + n - 1) digit result case
        while beg < len(res) and res[beg] == 0:
            beg += 1

        # convert each digit into a string 
        # turns [1, 2, 3, 4, 5] -> ["1", "2", "3", "4", "5"]
        res = map(str, res[beg:])

        return "".join(res)