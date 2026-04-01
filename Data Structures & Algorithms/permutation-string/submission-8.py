class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        

        counts1 = [0] * 26
        counts2 = [0] * 26
        for i in range(len(s1)):
            counts1[ord(s1[i]) - ord('a')] += 1
            counts2[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if counts1[i] == counts2[i]:
                matches += 1
        
        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[right]) - ord('a') 

            counts2[index] += 1
            if counts2[index] == counts1[index] + 1:
                matches -= 1
            elif counts2[index] == counts1[index]:
                matches += 1

            index = ord(s2[left]) - ord('a') 
            counts2[index] -= 1
            if counts2[index] == counts1[index] - 1:
                matches -= 1
            elif counts2[index] == counts1[index]:
                matches += 1
            left += 1
        return True if matches == 26 else False