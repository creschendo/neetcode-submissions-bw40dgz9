class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # create a map of the last index of each char
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        size = end = 0
        for i, c in enumerate(s):
            # increment size
            size += 1

            # update end, will be largest end
            # index seen thus far
            end = max(end, lastIndex[c])

            # if left pointer catches up, 
            # all occurences of all chars in 
            # current string are present
            if i == end:
                # add size of current string
                res.append(size)

                # set size to 0, start new string
                size = 0
        return res

        """
        last = {}
        for i, c in enumerate(s):
            last[c] = i

        sol = []
        left, right = 0, 0
        while left < len(s) and right < len(s):
            start = left
            right = max(right, last[s[left]])
            while left < right:
                right = max(right, last[s[left]])
                left += 1
            left = right + 1
            sol.append(right - start + 1)
        return sol
        """