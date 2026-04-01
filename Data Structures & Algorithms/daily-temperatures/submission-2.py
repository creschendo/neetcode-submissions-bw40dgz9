class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        sol = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            if not stack or temperatures[stack[-1]] >= temp:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < temp:
                    index = stack.pop()
                    sol[index] = i - index
                stack.append(i)
        return sol