class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        counts = {}
        for val in hand:
            counts[val] = counts.get(val, 0) + 1

        hand.sort()

        for val in hand:
            if val not in counts:
                continue
            counts[val] -= 1
            if counts[val] == 0:
                del counts[val]
            for i in range(1, groupSize):
                nextval = val + i
                if nextval not in counts:
                    return False
                counts[nextval] -= 1
                if counts[nextval] == 0:
                    del counts[nextval]
        return True
        """
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





