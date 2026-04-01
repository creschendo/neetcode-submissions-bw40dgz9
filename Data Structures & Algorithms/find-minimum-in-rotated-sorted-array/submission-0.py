class Solution:
    def findMin(self, nums: List[int]) -> int:
        sol = nums[0]
        left, right = 0, len(nums) - 1

        while left <= right:
            # section is sorted
            if nums[left] < nums[right]:
                sol = min(sol, nums[left])
                break
            
            # check if mid is the min
            mid = (left + right) // 2
            sol = min(sol, nums[mid])

            # if the left is sorted, then the rotation 
            # happened in the right
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
            
        return sol
