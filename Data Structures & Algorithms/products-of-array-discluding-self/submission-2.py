class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # create new result array
        res = [1] * len(nums)

        # calculate all prefix products, i.e. product of everything before the index
        # example:
        # original: [1, 2, 3, 4]
        # prefix:   [1, 1, 2, 6]
        pref = 1
        for i in range(len(nums)):
            res[i] = pref
            pref *= nums[i]
        
        # multiply result by suffix product, i.e. everything after the product
        # example:
        # original: [1, 2, 3, 4]
        # prefix:   [1, 1, 2, 6]
        # suffix:   [24, 12, 8, 6]
        # working backwards from prefix res
        #   6 x 1, since pos 4 has no suffix
        #   2 x 4, since suffix at pos 3 is 4
        #   1 x 12, since suffix at pos 2 is 12
        #   1 x 24, since suffix at pos 1 is 24
        suff = 1
        for j in range(len(nums)-1, -1, -1):
            res[j] = res[j] * suff
            suff *= nums[j]

        return res