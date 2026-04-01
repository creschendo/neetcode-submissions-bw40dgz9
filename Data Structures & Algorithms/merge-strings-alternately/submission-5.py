class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        sol = []
        i = 0
        while i < min(len(word1), len(word2)):
            sol.append(word1[i])
            sol.append(word2[i])
            i += 1

        sol.extend(word1[i:])
        sol.extend(word2[i:])
        return "".join(sol)