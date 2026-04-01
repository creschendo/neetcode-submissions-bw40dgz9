class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mappings = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        sol, part = [], []

        def dfs(i):
            # full string processed, add new combo to solution
            if i >= len(digits):
                sol.append("".join(part))
                return

            # retrieve all possible letters the current digit could be
            combos = mappings[digits[i]]

            # iterate through each letter, recursing on each possibility
            for letter in combos:

                # add letter possibility to current string being built
                part.append(letter)

                # recurse on next digit
                dfs(i + 1)

                # backtrack, removing processed letter and trying next letter
                part.pop()

        if digits:
            dfs(0)
        return sol