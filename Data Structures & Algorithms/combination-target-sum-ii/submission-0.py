class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []
        candidates.sort()

        def dfs(i, curr, total):
            if total == target:
                sol.append(curr.copy())
                return
            if total > target or i == len(candidates):
                return
            
            # choose to include the current index
            curr.append(candidates[i])
            dfs(i + 1, curr, total + candidates[i])

            # backtrack
            curr.pop()

            # since there are duplicates, we don't consider the 
            # same value as different elements, so move forward
            # until a new value is found
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curr, total)
        dfs(0, [], 0)
        return sol
            