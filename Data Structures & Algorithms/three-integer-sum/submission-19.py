class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []
        for i in range(len(nums)):
            if i > 0  and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    sol.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left + 1] == nums[left]:
                            left += 1
                    while right > left and nums[right - 1] == nums[right]:
                            right -= 1
                    left += 1
                    right -= 1
        return sol
            