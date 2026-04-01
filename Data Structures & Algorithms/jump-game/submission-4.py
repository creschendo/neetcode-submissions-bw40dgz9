class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        memo = {}
        def helper(index):
            if index in memo:
                return memo[index]
            if index == len(nums) - 1:
                return True
            elif nums[index] == 0:
                return False
            
            for i in range(1, nums[index] + 1):
                if helper(min(len(nums)-1, index + i)):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        
        return helper(0)
