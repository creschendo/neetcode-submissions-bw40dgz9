class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            if nums[mid] == target:
                return mid
            
            if (nums[left] <= target <= nums[mid]) or (target <= nums[mid] <= nums[left]):
                right = mid - 1
            else:
                left = mid + 1
        
        return -1