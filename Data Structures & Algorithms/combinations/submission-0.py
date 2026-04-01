class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol = []

        def helper(i, subset):
            nonlocal sol
            if len(subset) == k:
                sol.append(subset.copy())
                return
            for j in range(i, n + 1):
                subset.append(j)
                helper(j + 1, subset)
                subset.pop()

        helper(1, [])
        return sol

            