class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Iterate through the list in reverse, checking if the goal
        # cell can be reached by previous cells
        # If it can be reached, set the new goal to be the first cell that can reach it
        # If the goal is eventually moved to 0, then it must be reachable

        # Set goal to end initially
        goal = len(nums) - 1

        # Iterate in reverse from second to last square
        for i in range(len(nums) - 2, -1, -1):

            # If current square can reach current goal, set new goal
            if nums[i] >= goal - i:
                goal = i
        
        # Return if first square has been reached
        return goal == 0