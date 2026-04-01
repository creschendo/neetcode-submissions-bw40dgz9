class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor = n
        for i in range(n):
            xor ^= i
        for num in nums:
            xor ^= num
        return xor
