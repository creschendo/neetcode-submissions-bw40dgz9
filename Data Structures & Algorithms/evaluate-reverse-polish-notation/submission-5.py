class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # operator dictionary of lamda functions
        ops = {
               "+": lambda a, b: a + b, 
               "-": lambda a, b: a - b, 
               "/": lambda a, b: int(a / b),
               "*": lambda a, b: a * b
        }

        for token in tokens:
            # operand case, just push
            if token not in ops:
                stack.append(int(token))
            # operator case
            # pop top 2 and push result back to stack
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[token](a, b))
                
        # return final result
        return stack[-1]
            
