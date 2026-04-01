class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for string in strs:
            sort = "".join(sorted(string))
            groups[sort].append(string)
        
        return list(groups.values())