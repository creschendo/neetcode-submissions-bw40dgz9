class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                val = nums[i] + nums[left] + nums[right]
                if val < 0:
                    left += 1
                elif val > 0:
                    right -= 1
                elif val == 0:
                    triplet = [nums[i], nums[left], nums[right]] 
                    if triplet not in output:
                        output.append(triplet)
                    leftval = nums[left]
                    rightval = nums[right]
                    while  left < len(nums) and nums[left] == leftval:
                        left += 1
                    while rightval > i and nums[right] == rightval:
                        right -= 1
        return output