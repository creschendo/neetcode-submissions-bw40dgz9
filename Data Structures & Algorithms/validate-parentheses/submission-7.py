class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for val in s:
            if val == "}":
                if not stack or stack[-1] != "{":
                    return False
                stack.pop()
            elif val == "]":
                if not stack or stack[-1] != "[":
                    return False
                stack.pop()
            elif val == ")":
                if not stack or stack[-1] != "(":
                    return False
                stack.pop()
            else:
                stack.append(val)
        
        return False if stack else True