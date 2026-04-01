class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        return len(good) == 3

        """
        valid = []

        for triple in triplets:
            if (triple[0] <= target[0] 
            and triple[1] <= target[1] 
            and triple[2] <= target[2]):
                valid.append(triple)
        print(valid)
        
        trips = [1, 1, 1]
        for triple in valid:
            if triple[0] == target[0]:
                trips[0] = 0
            if triple[1] == target[1]:
                trips[1] = 0
            if triple[2] == target[2]:
                trips[2] = 0
        return trips == [0, 0, 0]
        """