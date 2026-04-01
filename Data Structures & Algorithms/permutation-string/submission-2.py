class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if s1 is longer, it's impossible for s2 to contain a permutation
        if len(s1) > len(s2) :
            return False


        # count up the occurences of each character
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # find how many matches exist in the first window
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        # iterate through all possible windows
        left = 0
        for right in range(len(s1), len(s2)):
            # if we've reached a full match, return true
            if matches == 26:
                return True
            
            # calculate index/char of the added right space
            index = ord(s2[right]) - ord('a')

            # add to the count in s2
            s2Count[index] += 1

            # if adding the character creates a match, add to it
            if s1Count[index] == s2Count[index]:
                matches += 1
            
            # adding the character causes overcount 
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # calculate the index/char of the left subtracted space
            index = ord(s2[left]) - ord('a')

            # subtract a count from that character
            s2Count[index] -= 1

            # if subtracting a character creates a match, add to it
            if s1Count[index] == s2Count[index]:
                matches += 1
            
            # subtracting character causes undercount
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            
            # moved the left pointer
            left += 1
        
        # return if the last window is a match
        return matches == 26