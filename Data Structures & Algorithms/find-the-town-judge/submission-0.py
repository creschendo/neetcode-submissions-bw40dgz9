class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ins = defaultdict(int)
        outs = defaultdict(int)

        for t in trust:
            ins[t[1]] = ins[t[1]] + 1
            outs[t[0]] = outs[t[0]] + 1

        for i in range(1, n + 1):
            if ins[i] == n - 1 and outs[i] == 0:
                return i
        return -1