class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for string in strs:
            sstr = ''.join(sorted(string))
            res[sstr].append(string)
        return list(res.values())