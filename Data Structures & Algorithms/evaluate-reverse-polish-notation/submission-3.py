class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        i = 0
        operators = {"+", "-", "/", "*"}
        while i < len(tokens):
            if (tokens[i] not in operators):
                print("appending: " + tokens[i])
                stack.append(tokens[i])
                i += 1
                continue
            else:
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                print("op1: " + str(op1))
                print("op2: " + str(op2))
                oper = tokens[i]
                if oper == "+":
                    stack.append(op1 + op2)
                elif oper == "-":
                    stack.append(op1 - op2)
                elif oper == "*":
                    stack.append(op1 * op2)
                elif oper == "/":
                    stack.append(op1 / op2)
                i += 1
        return int(stack[-1])
            
