class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # count all elements and store in a dictionary
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        # reverse the dictionary, now counts : element
        sorts = []
        for num, count in counts.items():
            sorts.append([count, num])
        
        # sort by counts
        sorts.sort()

        # append the value of the most frequent counts from sorts
        res = []
        for _ in range(k):
            res.append(sorts.pop()[1])
    
        return res
