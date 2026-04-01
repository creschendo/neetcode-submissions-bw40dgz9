class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack  = []

        for ast in asteroids:
            if not stack or ast > 0:
                stack.append(ast)
                continue
            while stack and ast < 0 < stack[-1]:
                right = stack[-1]
                left = ast

                if abs(right) > abs(left):
                    ast = 0
                    break
                
                elif abs(left) > abs(right):
                    stack.pop()
                    continue
                
                else:
                    stack.pop()
                    ast = 0
                    break
            if ast:
                stack.append(ast)
        return stack