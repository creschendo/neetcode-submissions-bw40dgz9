class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        sol = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append(i)
                continue
            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()
                sol[index] += (i - index)
            stack.append(i)
        return sol