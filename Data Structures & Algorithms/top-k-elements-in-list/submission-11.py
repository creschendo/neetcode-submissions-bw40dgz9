class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        most = max(counts.values())

        buckets = [[] for _ in range(most + 1)]

        for num, count in counts.items():
            buckets[count].append(num)

        sol = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                sol.append(num)
                if len(sol) == k:
                    return sol
        return sol
