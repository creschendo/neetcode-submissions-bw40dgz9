class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for ast in asteroids:
            if not stack or ast > 0:
                stack.append(ast)
            else:
                while stack and ast < 0 < stack[-1]:
                    # right moving and left moving asteroids
                    right = stack[-1]
                    left = ast

                    # right-moving asteroid is bigger, just skip
                    if abs(right) > abs(left):
                        ast = 0
                        break

                    # left moving asteroid is bigger, so pop the
                    # right moving and move on to next asteroid
                    elif abs(left) > abs(right):
                        stack.pop()
                        continue
                    
                    # two asteroids are equal, pop right and move on
                    else:
                        stack.pop()
                        ast = 0
                        break
                if ast:
                    stack.append(ast)

        return stack

            # check the signs of the new asteroid and the current top of the stack

            # the entire stack should have the same sign

            # while the signs of a collision are not the same, keep popping and colliding, 
            # keeping the larger of the two until either the stack is empty or the signs are 
            # the same