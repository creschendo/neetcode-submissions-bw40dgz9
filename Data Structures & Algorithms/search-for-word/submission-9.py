class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]  # ✅ defined once

        # ✅ early exit: check character frequencies
        board_count = Counter(c for row in board for c in row)
        word_count  = Counter(word)
        if any(word_count[c] > board_count[c] for c in word_count):
            return False

        # ✅ search the less-frequent end first
        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]

        def bt(row, col, curr):
            if curr == len(word):       # ✅ past last index = full match
                return True

            if (row < 0 or row >= m or
                col < 0 or col >= n or
                board[row][col] != word[curr]):
                return False

            tmp, board[row][col] = board[row][col], "#"  # ✅ mark in-place

            found = any(bt(row + x, col + y, curr + 1) for x, y in dirs)

            board[row][col] = tmp                        # ✅ restore
            return found

        return any(bt(i, j, 0) for i in range(m) for j in range(n))
        

