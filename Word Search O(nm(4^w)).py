def exist(self, board: List[List[str]], word: str) -> bool:
    def dfs(i, x, y):
        if i < len(word) and 0 <= x < len(board) and 0 <= y < len(board[0]) and word[i] == board[x][y]:
            char, board[x][y], i = board[x][y], None, i + 1
            res, board[x][y] = i == len(word) or dfs(i, x, y + 1) or dfs(i, x, y - 1) or dfs(i, x + 1, y) or dfs(i, x - 1, y), char

            return res

    for x in range(len(board)):
        for y in range(len(board[0])):
            if dfs(0, x, y):
                return True

    return False
