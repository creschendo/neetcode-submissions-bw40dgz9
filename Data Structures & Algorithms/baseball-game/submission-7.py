class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "+":
                v1 = stack[-1]
                v2 = stack[-2]
                stack.append(v1 + v2)
            elif op == "D":
                v1 = stack[-1]
                stack.append(v1 * 2)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        
        return sum(stack)



