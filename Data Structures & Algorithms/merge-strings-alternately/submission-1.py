class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1, p2, m, n = 0, 0, len(word1), len(word2)

        sol = []
        while p1 < m and p2 < n:
            sol.append(word1[p1])
            sol.append(word2[p2])
            p1 += 1
            p2 += 1
        

        sol.append(word1[p1:])
        sol.append(word2[p2:])
        
        return "".join(sol)
