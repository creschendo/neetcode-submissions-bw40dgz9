class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        for num in hand:
            start = num
            # find earliest possible start of the run including this number
            while count[start - 1]:
                start -= 1

            # try to make groups from start up to num
            while start <= num:

                # keep using same start until you can't, since it's minimum
                while count[start]:

                    # try to create a groupsize group from that start
                    for i in range(start, start + groupSize):

                        # needed value not there, return false
                        if not count[i]:
                            return False

                        # decrement used value
                        count[i] -= 1
                
                # current start has been used up, move to next
                start += 1
                
        return True

        """
        - O(nlog(n)) approach, due to sorting
        if len(hand) % groupSize:
            return False

        count = Counter(hand)
        hand.sort()
        for num in hand:
            if count[num]:
                for i in range(num, num + groupSize):
                    if not count[i]:
                        return False
                    count[i] -= 1
        return True

        [1, 2, 4, 2, 3, 5, 3, 4] gs = 4
        counts = {1:1, 2:2, 3:2, 4:2, 5:1}
        [1, 2, 2, 3, 3, 4, 4, 5] gs = 4

        outer loop (1)
        counts = {1:0, 2:2, 3:2, 4:2, 5:1}
            inner loop, i = 2
            counts = {1:0, 2:1, 3:2, 4:2, 5:1}
            inner loop, i = 3
            counts = {1:0, 2:1, 3:1, 4:2, 5:1}
            inner loop, i = 4
            counts = {1:0, 2:1, 3:1, 4:1, 5:1}
        outer loop(2)
        counts = {1:0, 2:0, 3:1, 4:1, 5:1}
            inner loop, i = 3
            counts = {1:0, 2:0, 3:0, 4:1, 5:1}
            inner loop, i = 4
            counts = {1:0, 2:0, 3:0, 4:0, 5:1}
            inner loop, i = 5
            counts = {1:0, 2:0, 3:0, 4:0, 5:0}
        """





