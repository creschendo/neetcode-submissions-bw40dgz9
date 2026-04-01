class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i in range(len(s) - 1, -1, -1):
            if s[i] in last:
                continue
            else:
                last[s[i]] = i
        print(last)

        sol = []
        left, right = 0, 0
        while left < len(s) and right < len(s):
            start = left
            seen = set(s[left])
            right = max(right, last[s[left]])
            while left < right:
                right = max(right, last[s[left]])
                seen.add(s[left])
                left += 1
            left = right + 1
            sol.append(right - start + 1)
        return sol