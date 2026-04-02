class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol = []
        curr = []
        def backtrack(closes, opens):
            # valid solution found
            if closes == opens == n:
                sol.append("".join(curr))
                return

            # use an open
            # only possible if opens used is less than n, otherwise 
            # invalid
            if opens < n:
                curr.append("(")
                backtrack(closes, opens + 1)
                curr.pop()
            
            # use a close
            # only possible if closes used so far is less than opens, 
            # otherwise prefix is invalid "())"
            if closes < opens:
                curr.append(")")
                backtrack(closes + 1, opens)
                curr.pop()

        backtrack(0, 0)
        return sol