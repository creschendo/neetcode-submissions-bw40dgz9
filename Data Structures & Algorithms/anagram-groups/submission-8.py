class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for st in strs:
            group = "".join(sorted(st))
            groups[group].append(st)

        return list(groups.values())