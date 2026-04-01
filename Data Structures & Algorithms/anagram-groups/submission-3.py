class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = defaultdict(list)
        for string in strs:
            sortedString = "".join(sorted(string))
            sol[sortedString].append(string)
        return list(sol.values())