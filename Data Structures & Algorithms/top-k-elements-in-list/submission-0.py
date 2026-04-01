class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        sorts = []
        for num, count in counts.items():
            sorts.append([count, num])
        
        sorts.sort()

        res = []
        for _ in range(k):
            res.append(sorts.pop()[1])

        return res
