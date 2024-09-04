def solveNQueens(self, n: int) -> List[List[str]]:
    boards, col, plus, minus = [], set(), set(), set()

    def dfs(i, board):
        if i == n:
            boards.append([''.join(line) for line in board])
            return
        
        for j in range(n):
            if j in col or i + j in plus or i - j in minus:
                continue
            col.add(j)
            plus.add(i + j)
            minus.add(i - j)
            board[i][j] = 'Q'

            dfs(i + 1, board)

            col.remove(j)
            plus.remove(i + j)
            minus.remove(i - j)
            board[i][j] = '.'

    dfs(0, [['.'] * n for _ in range(n)])

    return boards
