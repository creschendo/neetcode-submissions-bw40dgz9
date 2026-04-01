class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # if the total cost is higher than total gas, 
        # it's imposible, otherwise, there's one 
        # guaranteed solution
        if sum(gas) < sum(cost):
            return -1

        # track net gas level
        total = 0
        res = 0

        for i in range(len(gas)):
            # add to net gas
            total += (gas[i] - cost[i])

            # if negative, everything from 
            # res ... i is invalid, set new candidate
            # to i + 1
            if total < 0:
                total = 0
                res = i + 1

        
        return res