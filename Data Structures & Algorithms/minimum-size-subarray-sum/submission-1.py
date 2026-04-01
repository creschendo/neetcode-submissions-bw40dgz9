class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        minLen = float('inf')
        curr = 0
        for right in range(len(nums)):
            curr += nums[right]

            if curr >= target:
                minLen = min(minLen, (right - left + 1))

            while curr > target:
                curr -= nums[left]
                left += 1
                if curr >= target:
                    minLen = min(minLen, (right - left + 1))

        return minLen if minLen != float('inf') else 0
