class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, blue = 0, len(nums) - 1
        index = 0

        while index <= blue:
            # red case
            if nums[index] == 0:
                nums[red], nums[index] = nums[index], nums[red]
                red += 1
                index += 1

            # blue case
            elif nums[index] == 2:
                nums[blue], nums[index] = nums[index], nums[blue]
                blue -= 1
            
            # white case
            else:
                index += 1