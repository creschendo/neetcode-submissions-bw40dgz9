class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create an array of remainders from subtracting one element from target
        rems = [0] * len(nums)
        for i in range(len(nums)):
            # if the current number is in the remainders, then
            # nums[i] + nums(index(nums[i])) == target
            if nums[i] in rems and rems.index(nums[i]) != i:
                return [rems.index(nums[i]), i]
            
            # just add the remainder of the target minus current num
            else:
                rems[i] = target - nums[i]