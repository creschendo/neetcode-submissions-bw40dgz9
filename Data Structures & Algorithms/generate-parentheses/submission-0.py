class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol = []
        curr = []
        def backtrack(closes, opens):
            if closes == opens == n:
                sol.append("".join(curr))
                return
            if opens < n:
                curr.append("(")
                backtrack(closes, opens + 1)
                curr.pop()
            if closes < opens:
                curr.append(")")
                backtrack(closes + 1, opens)
                curr.pop()

        backtrack(0, 0)
        return sol