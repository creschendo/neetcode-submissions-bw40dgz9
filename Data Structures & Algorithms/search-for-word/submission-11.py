class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        # count word and board character occurences
        board_count = Counter(c for row in board for c in row)
        word_count  = Counter(word)

        # if word has more occurences, return false since impossible
        if any(word_count[c] > board_count[c] for c in word_count):
            return False

        # reverse word if rarer character is at the end,
        # reduces the number of dfs calls
        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]

        def bt(row, col, curr):
            # reached end of word, return True
            if curr == len(word):  
                return True

            # out of bounds, visited, or not equal
            # return False
            if (row < 0 or row >= m or
                col < 0 or col >= n or
                board[row][col] != word[curr]):
                return False

            # mark the board cell as visited
            tmp, board[row][col] = board[row][col], "#"  

            # check four directions
            found = any(bt(row + x, col + y, curr + 1) for x, y in dirs)

            # unmark visited on board
            board[row][col] = tmp    

            # return if valid path was found         
            return found

        # check every cell
        return any(bt(i, j, 0) for i in range(m) for j in range(n))
        

