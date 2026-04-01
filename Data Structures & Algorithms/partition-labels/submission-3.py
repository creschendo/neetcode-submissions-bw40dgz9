class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        size = end = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
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