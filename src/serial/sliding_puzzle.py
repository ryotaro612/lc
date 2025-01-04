from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        que = deque()

        que.append([board, 0])
        res = float('inf')
        visit = set()
        while que:
            board, counter = que.popleft()
            if board == [[1, 2, 3], [4, 5, 0]]:
                res = min(res, counter)
                continue

            for r in range(2):
                for c in range(3):
                    if board[r][c]:
                        continue
                    for n_r, n_c in [[r-1, c], [r, c+1], [r+1, c], [r, c-1]]:
                        if 0 <= n_r < 2 and 0 <= n_c < 3:
                            next_board = [list(row) for row in board]
                            next_board[r][c], next_board[n_r][n_c] = next_board[n_r][n_c], next_board[r][c]
                            if str(next_board) in visit:
                                continue
                            visit.add(str(next_board))
                            que.append([next_board, counter + 1])

        if res == float('inf'):
            return -1
        return res
