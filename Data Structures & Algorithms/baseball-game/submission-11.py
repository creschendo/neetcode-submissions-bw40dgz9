class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        sol = 0
        for op in operations:
            if op == "+":
                v1, v2 = stack[-1], stack[-2]
                stack.append(v1 + v2)
                sol += (v1 + v2)
            elif op == "D":
                v1 = stack[-1]
                stack.append(v1 * 2)
                sol += (v1 * 2)
            elif op == "C":
                sol -= stack.pop()
            else:
                stack.append(int(op))
                sol += (int(op))
        return sol