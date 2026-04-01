class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        smallest = 1
        nums.sort()
        for num in nums:
            if num == smallest:
                smallest += 1
            elif num > smallest:
                return smallest
        
        return smallest