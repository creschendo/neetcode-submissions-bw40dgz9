class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True

            # left is sorted
            if nums[left] < nums[mid]:

                # target is in sorted left
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1

                # target is in unsorted right
                else:
                    left = mid + 1
            
            # right is sorted
            elif nums[left] > nums[mid]:

                # target is in sorted right
                if nums[mid] < target <= nums[right]:
                    left = mid + 1

                # target is in unsorted left
                else:
                    right = mid - 1
            
            # left and mid are the same
            else:
                left += 1

        return False
