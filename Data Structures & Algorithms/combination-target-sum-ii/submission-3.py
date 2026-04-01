class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []

        candidates.sort()

        def bt(i, curr, total):
            if total == target:
                sol.append(list(curr))

            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if total + candidates[j] > target:
                    break
                curr.append(candidates[j])
                bt(j + 1, curr, total + candidates[j])
                curr.pop()
        
        bt(0, [], 0)
        return sol