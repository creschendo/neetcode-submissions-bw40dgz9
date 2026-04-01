class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        flip = []
        for num, count in counts.items():
            flip.append((count, num))
        
        flip.sort(reverse = True)

        sol = []

        for i in range(k):
            sol.append(flip[i][1])

        return sol