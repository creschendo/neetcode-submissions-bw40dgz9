class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        sol = []
        nums.sort()
        def bt(seen, curr):
            if len(curr) == len(nums):
                sol.append(list(curr))
                return
            
            for i in range(len(nums)):
                if i in seen:
                    continue
                if i and nums[i] == nums[i - 1] and (i - 1) not in seen:
                    continue
                curr.append(nums[i])
                seen.add(i)
                bt(seen, curr)
                seen.remove(i)
                curr.pop()
        
        bt(seen, [])
        return sol