class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            if not stack or ast > 0:
                stack.append(ast)
                continue
            while stack and stack[-1] > 0:
                if abs(stack[-1]) > abs(ast):
                    ast = 0
                    break
                elif abs(ast) > abs(stack[-1]):
                    stack.pop()
                    continue
                else:
                    stack.pop()
                    ast = 0  # both destroyed
                    break
            if ast:  # ✅ outside the while loop
                stack.append(ast)
        return stack