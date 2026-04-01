class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        sol = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if not stack or temperatures[stack[-1]] >= temperatures[i]:
                stack.append(i)
                continue
            else:
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    ind = stack.pop()
                    sol[ind] = i - ind
                stack.append(i)
        return sol