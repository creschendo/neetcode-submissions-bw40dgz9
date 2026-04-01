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

            if nums[mid] < nums[right]:
                right = mid - 1
            else:
                left = mid + 1
        return sol

