class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []

        # sort nums to use 2sum approach
        nums.sort()

        # fix the left value, set middle and right values to l, r
        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1

            # 2 sum approach
            while left < right:
                val = nums[i] + nums[left] + nums[right]

                # value is too small, move middle value right
                if val < 0:
                    left += 1

                # value is too large, move right value left
                elif val > 0:
                    right -= 1

                # found valid triplet
                elif val == 0:
                    output.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # move both pointers inward
                    left += 1
                    right -= 1
        return output