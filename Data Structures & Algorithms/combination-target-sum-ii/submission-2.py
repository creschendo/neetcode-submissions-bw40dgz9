class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        sol = []
        candidates.sort()
        def bt(total, curr, index):
            if total == target:
                sol.append(list(curr))
            elif total > target:
                return 
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                curr.append(candidates[i])
                bt(total + candidates[i], curr, i + 1)
                curr.pop()
        
        bt(0, [], 0)
        return sol