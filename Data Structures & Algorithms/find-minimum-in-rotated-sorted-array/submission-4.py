class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        sol = nums[0]
        while left <= right:
            if nums[left] < nums[right]:
                sol = min(sol, nums[left])
                break
            mid = (left + right) // 2
            sol = min(sol, nums[mid])
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return sol