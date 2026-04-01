class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        return max(counts, key = counts.get)