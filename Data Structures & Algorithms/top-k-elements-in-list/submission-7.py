class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # bucket sort
        # create n + 1 buckets, ranging from 0...n
        freq = [[] for i in range(len(nums) + 1)]

        # count up all frequencies
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # add number to its count bucket
        for num, cnt, in count.items():
            freq[cnt].append(num)
        
        res = []

        # iterate through all buckets in reverse
        for i in range(len(freq) - 1, 0, -1):

            # iterate through all values in a bucket
            for num in freq[i]:

                # add number to result
                res.append(num)

                # number of results is k, return
                if len(res) == k:
                    return res