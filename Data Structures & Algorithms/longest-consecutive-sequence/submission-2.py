class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # since the numbers can be in any order, create a set first
        numset = set(nums)

        # set max length
        maxlength = 0

        # iterate through all numbers
        for num in nums:

            # if we reach a number such that one less already exists, 
            # it's better to start at that number instead
            if (num - 1) not in numset:
                length = 1

                # keep adding to the length while consecutive elements exist
                while num + length in numset:
                    length += 1

                # set max
                maxlength = max(length, maxlength)
        
        return maxlength

                