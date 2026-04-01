class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countss, countst = {}, {}

        for i in range(len(s)):
            countss[s[i]] = countss.get(s[i], 0) + 1
            countst[t[i]] = countst.get(t[i], 0) + 1
        
        return countss == countst
