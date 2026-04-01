class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        used = [False] * len(nums)

        def backtrack(current):
            if len(current) == len(nums):
                res.add(tuple(current))
                return
            
            for i, num in enumerate(nums):
                if not used[i]:
                    current.append(num)
                    used[i] = True
                    backtrack(current)
                    current.pop()
                    used[i] = False
        
        backtrack([])
        return list(res)

        