class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        while True:
            find = False
            next_board = [[cell for cell in row] for row in board]
            n_row, n_col = len(board), len(board[0])

            for r in range(n_row):
                for c in range(n_col):
                    if c < n_col - 2:
                        if (
                            board[r][c]
                            and board[r][c] == board[r][c + 1] == board[r][c + 2]
                        ):
                            next_board[r][c] = next_board[r][c + 1] = next_board[r][
                                c + 2
                            ] = 0
                            find = True
                    if r < n_row - 2:
                        if (
                            board[r][c]
                            and board[r][c] == board[r + 1][c] == board[r + 2][c]
                        ):
                            next_board[r][c] = next_board[r + 1][c] = next_board[r + 2][
                                c
                            ] = 0
                            find = True
            if not find:
                break

            for c in range(n_col):
                col = []
                for r in range(n_row - 1, -1, -1):
                    if next_board[r][c]:
                        col.append(next_board[r][c])
                while len(col) < n_row:
                    col.append(0)
                for r in range(n_row - 1, -1, -1):
                    next_board[r][c] = col[n_row - 1 - r]
            board = next_board
        return board
