class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = set(nums)

        best = 0
        for num in nums:
            if num - 1 in vals:
                continue
            curr = 1
            while num + 1 in vals:
                num += 1
                curr += 1
            best = max(best, curr)
        
        return best
