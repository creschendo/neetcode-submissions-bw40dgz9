class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # default dict makes a map that fills with default values to avoid no key errors
        # keys: sorted strings
        # values: arrays of original strings with same keys
        res = defaultdict(list)

        for string in strs:
            # sort the characters of each string alphabetically
            # join them into a single string
            sstr = ''.join(sorted(string))

            # use the single string as a key in the dictionary to store
            # all strings with the same sorted key value
            # all anagrams will fall into the same array
            res[sstr].append(string)
        
        # return a list of all values, i.e. all arrays 
        return list(res.values())