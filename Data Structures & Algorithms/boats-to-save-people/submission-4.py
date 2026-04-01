class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        buckets = [0] * (max(people) + 1)

        for p in people:
            buckets[p] += 1

        index, i = 0, 1
        while index < len(people):
            while buckets[i] == 0:
                i += 1
            people[index] = i
            buckets[i] -= 1
            index += 1
        print(people)
        sol = 0
        left, right = 0, len(people) - 1

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            sol += 1

        return sol