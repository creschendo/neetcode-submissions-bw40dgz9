class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = {}
        sol = []
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for n, c in counts.items():
            if c > (len(nums) // 3):
                sol.append(n)

        return sol