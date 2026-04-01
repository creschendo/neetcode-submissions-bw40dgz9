class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        curr = 0
        best = float('inf')
        left = 0

        for right in range(len(nums)):
            curr += nums[right]

            while curr >= target:
                best = min(best, right - left + 1)
                curr -= nums[left]
                left += 1
            
        return best if best != float('inf') else 0