class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if s1 longer, impossible
        if len(s1) > len(s2):
            return False


        # count occurences for both
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        # count current matches
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        left  = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # add counts of right character coming in
            index = ord(s2[right]) - ord('a')
            s2Count[index] += 1

            # addition causes a new equality
            if s1Count[index] == s2Count[index]:
                matches += 1

            # addition cause match to be lost
            elif s2Count[index] == s1Count[index] + 1:
                matches -= 1

            # remove counts of left character leaving window
            index = ord(s2[left]) - ord('a')
            s2Count[index] -= 1

            # subtraction causes new match
            if s1Count[index] == s2Count[index]:
                matches += 1

            # subtraction causes match to be lost
            elif s2Count[index] == s1Count[index] - 1:
                matches -= 1   
            left += 1
        return matches == 26