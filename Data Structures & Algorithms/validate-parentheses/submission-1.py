class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = ['(', '{', '[']
        for char in s:
            if char in opens:
                stack.append(char)
            elif char == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif char == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            elif char == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        return False if stack else True