class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, total = 0, 0
        best = float('inf')

        for right in range(len(nums)):
            total += nums[right]
            print(nums[right])
            while total >= target:
                best = min(right - left + 1, best)
                total -= nums[left]
                left += 1

        return 0 if best == float("inf") else best
