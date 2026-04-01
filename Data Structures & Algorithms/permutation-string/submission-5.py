class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        counts1 = [0] * 26
        for c in s1:
            counts1[ord(c) - ord('a')] += 1
        
        left = 0
        counts2 = [0] * 26

        for right in range(len(s2)):
            counts2[ord(s2[right]) - ord('a')] += 1

            if counts2 == counts1:
                return True
            
            if (right - left + 1) == len(s1):
                counts2[ord(s2[left]) - ord('a')] -= 1
                left += 1
        return False
            
