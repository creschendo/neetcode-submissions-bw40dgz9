class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
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