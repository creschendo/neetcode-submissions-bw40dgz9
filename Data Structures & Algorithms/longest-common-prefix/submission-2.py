class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        pref = strs[0]

        for string in strs[1:]:
            i = 0

            while i < min(len(string), len(pref)) and string[i] == pref[i]:
                i += 1
            
            pref = pref[:i]
            
        return pref