class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        # count up all occurences
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        # bucket sort by frequency
        freq = [[] for i in range(len(nums) + 1)]
        for num, count in counts.items():
            freq[count].append(num)
        
        sol = []

        # take top k from buckets
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                sol.append(num)

                if len(sol) == k:
                    return sol 