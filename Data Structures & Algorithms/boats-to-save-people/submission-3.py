class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        """
        BUCKET SORT OPTIMIZATION TO MAKE O(n) TIME INSTEAD OF NLOGN FOR SORT
        biggest = max(people)
        counts = [0] * (biggest + 1)

        for p in people:
            counts[p] += 1
        

        idx, i = 0, 1
        while idx < len(people):
            while counts[i] == 0:
                i += 1
            people[idx] = i
            counts[i] -= 1
            idx += 1
        """
        people.sort()


        sol = 0
        left, right = 0, len(people) - 1

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1 
            right -= 1
            sol += 1
        
        return sol



