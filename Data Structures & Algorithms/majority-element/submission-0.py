class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

            if counts[num] == (len(nums) // 2) + 1:
                return num
            
        return 0