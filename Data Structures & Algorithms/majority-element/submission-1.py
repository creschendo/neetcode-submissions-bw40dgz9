class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer Moore Voting Algo
        # O(n) time, O(n) space
        sol = count = 0

        for num in nums:
            if count == 0:
                sol = num
            count += (1 if num == sol else -1)
        
        return sol

        """
        O(n) time, 
        O(n) space
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

            if counts[num] == (len(nums) // 2) + 1:
                return num
            
        return 0

        """