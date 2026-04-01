class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        sol = []

        one, two = 0, 0 

        while one < len(word1) and two < len(word2):
            sol.append(word1[one])
            sol.append(word2[two])
            one += 1
            two += 1
        
        sol.extend(word1[one:])
        sol.extend(word2[two:])

        return "".join(sol)