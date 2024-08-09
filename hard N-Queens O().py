def solveNQueens(self, n: int) -> List[List[str]]:
    boards, col, plus, minus = [], set(), set(), set()

    def dfs(i, board):
        if i == n:
            boards.append([''.join(line) for line in board])
        else:
            for j in range(n):
                if j not in col and i + j not in plus and i - j not in minus:
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
