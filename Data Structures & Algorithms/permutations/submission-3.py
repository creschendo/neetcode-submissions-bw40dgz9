class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        seen  = set()
        sol = []

        def bt(seen, curr):
            if len(curr) == len(nums):
                sol.append(list(curr))
                return

            for i in range(len(nums)):
                if i in seen:
                    continue
                seen.add(i)
                curr.append(nums[i])
                bt(seen, curr)
                seen.remove(i)
                curr.pop()
        
        bt(seen, [])
        return sol
