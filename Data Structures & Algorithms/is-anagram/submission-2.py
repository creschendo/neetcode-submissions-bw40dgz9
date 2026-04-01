class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}

        # count the characters of each word with maps
        for char in s:
            map1[char] = map1.get(char, 0) + 1
        for char in t:
            map2[char] = map2.get(char, 0) + 1

        # since hashmap, if all counts are the same, the words are anagrams
        return map1 == map2