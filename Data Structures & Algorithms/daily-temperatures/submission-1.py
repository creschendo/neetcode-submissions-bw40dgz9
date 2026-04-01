class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack keeps track of indices, not values
        stack = []

        # initialize solution to all zeroes
        sol = [0] * len(temperatures)

        for i in range(len(temperatures)):
            # if the stack is empty or the current is smaller, just push
            if not stack or temperatures[stack[-1]] >= temperatures[i]:
                stack.append(i)

            # the current temp is higher, so pop and update solution until all lower
            # index values have been popped 
            else:
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    index = stack.pop()
                    sol[index] = i - index
                # push current to the stack
                stack.append(i)
        
        # return solution
        return sol
