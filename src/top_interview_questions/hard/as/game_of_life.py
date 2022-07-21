"""
Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

[[0,1,0],
 [0,0,1],
 [1,1,1],
 [0,0,0]]
      0, 1, 2, 3
cur   0  1  0  1
next  1  1  1  0
"""
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n_row, n_col = len(board),len(board[0])
        
        for r in range(n_row):
            for c in range(n_col):
                live, dead = self.countNeighbors(r, c, board)
                #print(r, c, live, dead)
                if board[r][c] == 1 and (live < 2 or 3 < live):
                    board[r][c] = 3
                elif board[r][c] == 1 and live in {2, 3}:
                    board[r][c] = 1
                elif board[r][c] == 0 and live == 3:
                    board[r][c] = 2
        
        for r in range(n_row):
            for c in range(n_col):
                if board[r][c] == 2:
                    board[r][c] = 1
                elif board[r][c] == 3:
                    board[r][c] = 0
        
    
    def countNeighbors(self, r, c, board):
        n_row, n_col = len(board), len(board[0])
        live, dead = 0, 0 
        for ne_r, ne_c in ((r + delta_r, c + delta_c) 
                           for delta_r in range(-1, 2) 
                           for delta_c in range(-1, 2)):
            if ne_r == r and ne_c == c:
                continue
            if 0 <= ne_r < n_row and 0 <= ne_c < n_col:
                if board[ne_r][ne_c] in {1, 3}:
                    live += 1
                else:
                    dead += 1
        return live, dead
