class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol = []

        def bt(i, curr):
            if len(curr) == k:
                sol.append(list(curr))
                return

            for j in range(i, n + 1):
                curr.append(j)
                bt(j + 1, curr)
                curr.pop()
        
        bt(1, [])
        return sol